var MAP_APP = {};

Vue.use(VueI18n)
// Ready translated locale messages
const messages = {
  en: {
    message: {
      date: 'Date',
      name: 'Name',
      code: 'Code',
      wages: 'Wages',
      inhabitans: 'Inhabitans',
      productive_inhabitans: 'Productive inhabitans',
      unemployed: 'Unemployed',
      vacancies: 'Vacancies',
      unemployment: 'Unemployment',
      applications_per_vacancy: 'Applications per vacancy',
      house_number: "House number",
      orientation_number: "Orientation number",
      city: "City",
      city_code: "City - code",
      zipcode: "Zip code",
      administrative_id: "ID",
      previous: "Previous",
      next: "Next",
      street: "Street"
    }
  },
  cs: {
    message: {
      date: 'Datum',
      name: 'Jméno',
      code: 'Kód',
      wages: 'Pracovní síla',
      inhabitans: 'Počet obyvatel',
      productive_inhabitans: 'Počet obyvatel v produktivním věku',
      unemployed: 'Počet nezaměstnaných',
      vacancies: 'Počet pracovních míst',
      unemployment: 'Nezaměstnanost',
      applications_per_vacancy: 'Počet žádostí na jedno pracovní místo',
      house_number: "Číslo domovní",
      orientation_number: "Číslo orientační",
      city: "Obec",
      city_code: "Kód obce",
      zipcode: "PSČ",
      administrative_id: "ID",
      previous: "Předchozí",
      next: "Další",
      street: "Ulice"
    }
  }
}

// Create VueI18n instance with options
const i18n = new VueI18n({
  locale: 'cs', // set locale
  messages, // set locale messages
})

Vue.component("feature-row", {
  props: ["feature", "features", "layer"],
  active_el: 0,
  methods: {
    "onRowClick": function(id) {
      let layerFeatures = this.layer.getLayers();
      for (var i = 0; i < layerFeatures.length - 1; i++) {
        var f = layerFeatures[i];
        f.setStyle(vue_app.styles.default);
        if (f.feature == this.feature) {
          f.setStyle(vue_app.styles.highlight);
        }
      }
    },
    "activate": function(el) {
      this.active_el = el;
    }
  },
  template: "<tr v-on:click='onRowClick()' ><td v-for='attr in feature.properties'>{{ attr }}</td></tr>"
});

Vue.component("feature-column", {
    props: ["attribute"],
    methods: {
      "click": function(attribute) {
        vue_app.legend_column = attribute;
      }
    },
    template: "<th class=\"attributes\" v-on:click=\"click(attribute)\"><a href=\"#\">{{ $t( String( \"message.\" + attribute) ) }}</a></th>"
});

let pages = Vue.component("pages", {
    props: ["count", "next", "previous", "DESC"],
    methods: {
      /** if the ordering is descending, return the other link */
      "getNext": function() {
        return (DESC ? this.previous : this.next);
      },
      "getPrevious": function() {
        return (DESC ? this.next : this.previous);
      },
      "onClicked": function(link) {
        if (link) {
          vue_app.setDataLink(link);
        }
      },
      "isNextDisabled": function(){
        return (this.getNext() ? false : true);
      },
      "isPreviousDisabled": function(){
        return (this.getPrevious() ? false : true);
      }
    },
    template: "<div class=\"btn-group\">" +
                '<button type="button" class="btn btn-outline-primary" v-on:click=\"onClicked(getPrevious())\" v-bind:disabled="isPreviousDisabled()">{{ $t( \"message.previous\" ) }}</button>' +
                '<button type="button" class="btn btn-outline-primary" v-on:click=\"onClicked(getNext())\" v-bind:disabled="isNextDisabled()">{{ $t( \"message.next\" ) }}</button>' +
              '</div>'
});


Vue.component("api-links", {
    props: ["OBJECT_NAME"],
    methods: {
      "openWindow": function(type) {
        if (type === "apidoc") {
          let url = '/apidoc/';
        }
        else {
          let url =  '/api/' + OBJECT_NAME.replace(/\/$/, '') + '.' + type;
        }
        window.open(url, '_blank');
      }
    },
    template: '<div class="btn-group">' +
        '<button type="button" class="btn btn-outline-primary" v-on:click="openWindow(\'apidoc\')" >API (Swagger)</button>'+
        '<button type="button" class="btn btn-outline-primary" v-on:click="openWindow(\'json\')" >(Geo)JSON</button>'+
        '<button type="button" class="btn btn-outline-primary" v-on:click="openWindow(\'xlsx\')" >XLSX</button>'+
      '</div>'
});

/**
 * initialize table from geojson variable data
 */
var vue_app = new Vue({
  i18n,
  delimiters: ['[[', ']]'],
  el: '#navigation_table',
  data: {
    title: 'Welcome to My Journal',
    data_link: '/api/' + OBJECT_NAME,
    features: null,
    data: null,
    legend_column: null,
    min: null,
    max: null,
    count: null,
    next: null,
    previous: null,
    map: window.MAP,
    object_name: null,
    layer: null,
    styles: {
      default: {
          weight: 3,
          color: '#66c',
          dashArray: '',
          fillOpacity: 0.3
        },
        highlight: {
            weight: 5,
            color: '#c66',
            dashArray: '',
            fillOpacity: 0.5
        }
      }
  },
  mounted () {
    this.setDataLink();
  },
  methods: {
    "setDataLink": function(data_link) {
      document.getElementById("spinner").style.display = "block";
      if (data_link) {
        this.data_link = data_link;
      }
      axios
        .get(this.data_link)
        .then(response => (this.data = response.data))
        .then(this.initMap);
    },
    "onColumnClick": function(name) {
      this.legend_column = name;
    },
    "initMap": function() {

      if (this.layer) {
        this.layer.removeFrom(this.map);
      }


      this.features  = this.data.features ? this.data : this.data.results;

      this.layer = L.markerClusterGroup();
      this.layer.addLayer(L.geoJSON(this.features, {
        onEachFeature: this.onEachFeature,
        style: this.getFeatureStyle
      }));
      this.map.addLayer(this.layer);

      this.setPages(this.data.count, this.data.next, this.data.previous);

      let clsname = document.getElementById("cigeo_map").className;

      this.initInfoPanel();

      document.getElementById("spinner").style.display = "none";
    },
    "initInfoPanel": function() {
      if (this.info) {
        this.map.removeControl(this.info);
      }

      this.info = L.control();

      this.info.onAdd = function (map) {
          this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
          this.update();
          return this._div;
      };

      // method that we will use to update the control based on feature properties passed
      this.info.update = function (props) {
          this._div.innerHTML = "";
          if (props) {
            var tbl = "";
            for (var k in props) {
              tbl += "<tr><th>" + k + "</th><td>"+ props[k] + "</td></tr>";
              //this._div.innerHTML += "<tr><th>" + k + "</th><td>"+ props[k] + "</td></tr>";
            }
            this._div.innerHTML = "<table class=\"table stripped table-sm\">" + tbl + "</table>";
          } else {
            this._div.innerHTML = "";
          }
      };

      this.info.addTo(this.map);
    },
    "initLegendPanel": function() {

      if (this.legend) {
        this.map.removeControl(this.legend);
      }
      this.legend = L.control({position: 'bottomright'});
      this.legend.vue_app = this;

      this.legend.onAdd = function (map) {

          var div = L.DomUtil.create('div', 'info legend'),
              grades = [0, 1, 2, 3, 4, 5, 6, 7].map(
                function(i) {
                    return Math.round(this.vue_app.min + (this.vue_app.max - this.vue_app.min)/8*i)
                }
              );
              labels = [];

          // loop through our density intervals and generate a label with a colored square for each interval
          for (var i = 0; i < grades.length; i++) {
              div.innerHTML +=
                  '<i style="background:' + this.vue_app.getFeatureColor(grades[i]) + '">&nbsp;</i> ' +
                  grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1]  : '+')+"<br/>";
          }

          return div;
      };

      this.legend.addTo(this.map);
    },
    "setPages": function(count, next, previous) {
      this.count = count;
      this.next = next;
      this.previous = previous;
      pages.next = this.next;
      pages.previous = this.previous;
    },
    "getDataExtent": function(attribute) {
        var min;
        var max;
        let data = this.features.features.map(
            function(f) {
                return Number(f.properties[attribute]);
            });
        return [Math.min(...data), Math.max(...data)];

        try {
          for (var i = 0; i < this.features.features.length; i++) {
            var f = this.features.features[i];
            if (min != null) {
              if (f.properties[attribute] < min) {
                min = Math.round(Number(f.properties[attribute]));
              }
            }
            else {
              min =  Math.round(Number(f.properties[attribute]));
            }

            if (max) {
              if (f.properties[attribute] > max) {
                min = Math.round((f.properties[attribute]));
              }
            }
            else {
                max = Math.round(Number(f.properties[attribute]));
            }
          }
          return [min, max];
        } catch (e) {
          console.log(e);
          return [undefined, undefined];
        }
      },
      "onEachFeature": function(feature, layer) {
        layer.on({
            mouseover: this.highlightFeature,
            mouseout: this.resetHighlight,
            click: this.zoomToFeature
        });
    },
    /**
     * get feature style based on its data and selected legend column
     */
    "getFeatureStyle": function(feature) {
      var style = this.styles.default;
      if (this.legend_column && feature.properties[this.legend_column]) {
              style.fillColor = this.getFeatureColor(feature.properties[this.legend_column]);
      }

      return style;
    },
    "getFeatureColor": function(value) {
        var step = (this.max - this.min)/8;
        var color;
        if (value < this.min + 0*step) {
          color = '#800026';
        }
        else if (value < this.min + 1*step) {
          color = '#BD0026';
        }
        else if (value < this.min + 2*step) {
          color = '#E31A1C';
        }
        else if (value < this.min + 3*step) {
          color = '#FC4E2A';
        }
        else if (value < this.min + 4*step) {
          color = '#FD8D3C';
        }
        else if (value < this.min + 5*step) {
          color = '#FEB24C';
        }
        else if (value < this.min + 6*step) {
          color = '#FED976';
        }
        else {
          color = '#FFEDA0';
        }
        return color;
    },

    "highlightFeature": function(e) {

      var layer = e.target;

      layer.setStyle(this.styles.highlight);

      if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
          layer.bringToFront();
      }
      this.info.update(layer.feature.properties);
    },

    "resetHighlight": function(e) {
        e.target.setStyle(this.getFeatureStyle(e.target.feature));
        this.info.update();
    },
    "zoomToFeature": function (e) {
        this.map.fitBounds(e.target.getBounds());
    },
  },
  watch: {
    legend_column: function(name) {
      var mm =  this.getDataExtent(name);
      if (mm[0] !== undefined) {
        this.min = mm[0];
        this.max = mm[1];

        let layerFeatures = this.layer.getLayers();
        for (var i = 0; i < layerFeatures.length; i++) {
          l = layerFeatures[i];
          l.setStyle(this.getFeatureStyle(l.feature));
        }
        this.initLegendPanel();
      } else {
        this.min = mm[0];
        this.max = mm[1];
      }
    },
    "map": function(map) {
      this.map = map;
    }
  }
});

var map_init = function(map) {
  
  map._layersMaxZoom = 20;
  vue_app.map = map;
};



