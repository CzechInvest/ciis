from django.core.management.base import BaseCommand, CommandError
from dotacni_matice.models.matrix import *
from openpyxl import load_workbook
import datetime
import re

class Command(BaseCommand):
    help = 'Import initial data sets to database'

    def add_arguments(self, parser):
        parser.add_argument('data', type=str, help="data file")

    def handle(self, *args, **options):

        file_name = options["data"]
        wb = load_workbook(file_name)
        all_obj = self.titles(wb, "Matice")
        #DotacniTitul.objects.bulk_create(all_obj)
        self.stdout.write(self.style.SUCCESS('Successfully imported data'))

    def titles(self, wb, tab):

        data = wb.get_sheet_by_name(tab)
        out_data = []

        counter = 0
        for row in data:
            counter += 1
            if counter <= 3:
                continue

            print(row[4], row[4].value)
            (today, changed, competence, program, name, type_, area, mip, mp, sp, vp,
                    nno, public, semafor, call, call_from, call_to, full_from,
                    full_to, allocation, min_, max_, form, historie, regime,
                    supported, eligible, ineligible, pkn, pkv, url, comment,
                    note, afc, ipo, investment, noninvestment, sallery,
                    personal, education, consultation, research, real_estate,
                    machines, construction_works, administration, hw, sw, flat,
                    marketing) = row[0:50]

            competence = self.competence(competence)
            program = self.program(program)
            type_ = self.get_type(type_)
            area = self.clean(area)
            mip = self.max_support(mip)
            mp = self.max_support(mp)
            sp = self.max_support(sp)
            vp = self.max_support(vp)
            nno = self.max_support(nno)
            nno = self.max_support(nno)
            public = self.max_support(public)
            semafor = self.semafor(semafor)
            pkn = self.pk(pkn)
            pkv = self.pk(pkv)

            min_ = self.clean(min_)
            max_ = self.clean(max_)
            if min_ and type(min_) == type("") and min_.find("0,2 mil.") > -1:
                if min_ == "?":
                    min_ = None
                min_ = 0.2
            if max_:
                if max_ == "?":
                    max_ =  None
                if max_ == "=50*27":
                    max_ = 50*27
                if max_ == "=50*28":
                    max_ = 50*28
                if max_ == "25-80":
                    max_ = 25-80
                if max_ == "=25*75":
                    max_ = 25*75
                if max_ == "=50*25":
                    max_ = 50*25
                if max_ == "50 (max. dotace)":
                    max_ = 50
                if max_ == "14,2/15/40":
                    max_ = 40
                if max_:
                    max_ = float(max_)

            allocated = self.clean(allocation)
            if allocated:
                if allocated == "?":
                    allocated = None
                elif allocated == "=15*25":
                    allocated = 15 * 25
                elif allocated == "328,125  (alokace už byla překročena)":
                    allocated = 125
                else:
                    allocated = float(allocated)

            changed=str(changed.value).split(" ")[0]
            date_call=str(call.value).split(" ")[0]
            date_pref_from=str(call_from.value).split(" ")[0]
            date_pref_to=str(call_to.value).split(" ")[0]
            date_full_from=str(full_from.value).split(" ")[0]
            date_full_to=str(full_to.value).split(" ")[0]

            (changed, date_call, date_pref_from, date_pref_to,
                    date_full_from, date_full_to) = self.test_dates(
                            changed, date_call, date_pref_from, date_pref_to,
                    date_full_from, date_full_to)

            dt = DotacniTitul.objects.create(
                changed=changed,
                competence=competence,
                program=program,
                name=self.clean(name),
                type=type_,
                area=area,
                mip=mip,
                mp=mp,
                sp=sp,
                vp=vp,
                nno=nno,
                public=public,
                #state=semafor,
                date_call=date_call,
                date_pref_from=date_pref_from,
                date_pref_to=date_pref_to,
                date_full_from=date_full_from,
                date_full_to=date_full_to,
                allocated=allocated,
                min=min_,
                max=max_,
                form=self.clean(form),
                history=self.clean(historie),
                regime=self.clean(regime),
                supported_activities=self.clean(supported),
                eligible_costs=self.clean(eligible),
                ineligible_costs=self.clean(ineligible),
                pkn=pkn,
                pkv=pkv,
                url=self.clean(url),
                comment=self.clean(comment),
                note=self.clean(note),
                afc=self.filtr(afc),
                ipo=self.filtr(ipo),
                investment=self.filtr(investment),
                noninvestment=self.filtr(noninvestment),
                remuneration=self.filtr(sallery),
                personal_costs=self.filtr(personal),
                education=self.filtr(education),
                consultation=self.filtr(consultation),
                research=self.filtr(research),
                property=self.filtr(real_estate),
                machines=self.filtr(machines),
                construction=self.filtr(construction_works),
                administration=self.filtr(administration),
                hw=self.filtr(hw),
                sw=self.filtr(sw),
                lump=self.filtr(flat),
                marketing=self.filtr(marketing)
                )

            out_data.append(dt)
        print(len(out_data))
        return out_data

    def test_dates(self, *args):

        results = []
        valid = re.compile(r"^\d{4}-\d{2}-\d{2}$")
        for arg in args:
            if arg == "2019?":
                arg = "2019-01-01"
            elif arg == "2015":
                arg = "2015-01-01"
            elif arg == "30.1.201915.04.2018":
                arg = "2019-01-30"
            elif arg == "8.11..2016":
                arg = "2016-11-08"



            if arg == "None":
                arg = None
            elif arg is not None:
                result = valid.match(arg)
                if result == None and arg != None:
                    raise Exception(f"Wrong date format {arg}")
            #if arg is None:
            #    arg = "2019-01-01"
            results.append(arg)
        return results


    def filtr(self, val):
        val = self.clean(val)
        if val and val != "n" and val != "x":
            return True
        elif val == "n" or val == "x":
            return False
        else:
            return None


    def pk(self, val):

        val = self.clean(val)
        if not val:
            return val

        if val == "---":
            return None

        if type(val) == type("") and val.find("a)\n32100") == 0:
            return 32100
        if type(val) == type("") and val.find("a)\n36010") == 0:
            return 36010

        sepl = ""
        if type(val) == type(""):

            if val.find(",") > -1:
                sepl = ","
            elif val.find(".") > -1:
                sepl = "."
            elif val.find(";") > -1:
                sepl = ";"
            elif val.find(" ") > -1:
                sepl = " "
            elif val.find("\n") > -1:
                sepl = "\n"
            elif val == "x":
                return None
            else:
                return int(val)
        else:
            val = int(val)
            return val

        if val.find("6 25 00") > -1:
                return 62500
        if val.find("6 00 00") > -1:
                return 60000
        if val.find("50001") > -1:
                return 50001
        if val.find("33902") > -1:
            return 33902
        if val.find("34610") > - 1:
            return 34610

        return int(self.clean(val.split(sepl)[0]))



    def clean(self, val):

        if val:
            if hasattr(val, "value"):
                if not val.value:
                    return val.value
                else:
                    if type(val.value) == type(""):
                        val = val.value.strip()
                    else:
                        val = val.value
            else:
                if type(val) == type(""):
                    val = val.strip()

            if val == "n":
                val = None

            if val == "":
                val = None

            if val == "a":
                val = True

            if val == "n":
                val = False
            if val == "?":
                val = None
        else:
            val = None

        return val

    def max_support(self, val):
        val = self.clean(val)
        if val == False or val == None:
            return None
        if val == True:
            val = 1
        if val == "?":
            val = -1

        if val == "dle aktivity":
            val = -2
        if type(val) == type(""):
            if val.find("až") > -1:
                val = int(val.replace("až", ""))
            elif val.find("Dotace je poskytována") > -1:
                return None
            elif val.find("85%") > -1:
                val = 85
            else:
                print("###", val)

        mylist = (-3, -2, -1, 1, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80,
                85, 90, 95, 100)
        val = min(mylist, key=lambda x:abs(x-val))
        return val

    def competence(self, competence):

        competence = self.clean(competence)
        if competence:
            cs = Competence.objects.filter(competence=competence)
            if len(cs) == 0:
                c = Competence.objects.create(competence=competence)
            else:
                c = cs[0]
            return c
        else:
            return None

    def get_type(self, mytype):
        mytype = self.clean(mytype)

        if mytype:
            cs = CallType.objects.filter(type=mytype)
            if len(cs) == 0:
                c = CallType.objects.create(type=mytype)
            else:
                c = cs[0]
            return c
        else:
            return None


    
    def program(self, program):

        program = self.clean(program)
        if program:
            ps = Program.objects.filter(program=program)
            if len(ps) == 0:
                p = Program.objects.create(program=program)
            else:
                p = ps[0]
            return p
        else:
            return None

    def semafor(self, semafor):
        val = self.clean(semafor).lower()
        if val == "plánováno":
            val = 10
        elif val == "sběr plná":
            val = 20
        elif val == "vyhlášeno":
            val = 30
        elif val == "ukončeno":
            val = 40

        return val
