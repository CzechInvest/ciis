var MAP_APP = {};

Vue.component("feature-row", {
  props: ["feature", "features", "layer"],
  methods: {
    "onRowClick": function(id) {
      var feature;
      for (var i in this.layer._layers) {
        var l = this.layer._layers[i];
        if (l.feature.properties.code == id) {
          feature = l;
        }
        l.setStyle({'color': 'blue','weight': 2,'opacity': 1});
      }
      feature.setStyle({ 'color': 'red', 'weight': 2, 'opacity': 1 });
    }
  },
  template: "<tr v-on:click='onRowClick(feature.id)' ><td v-for='attr in feature.properties'>{{ attr }}</td></tr>"
});

Vue.component("feature-column", {
    props: ["attribute"],
    methods: {
    },
    template: "<th>{{ attribute }}</th>"
});

/**
 * initialize table from geojson variable data
 */
var vue_app = new Vue({
  delimiters: ['[[', ']]'],
  el: '#table',
  data: {
    title: 'Welcome to My Journal',
    features: geojson,
    legend_column: null,
    min: null,
    max: null,
    map: null,
    layer: null,
  },
  methods: {
    "onColumnClick": function(name) {
      this.legend_column = name;
    },
    "getMM": function(attribute) {
        var min;
        var max;
        for (var i = 0; i < this.features.features.length; i++) { 
          var f = this.features.features[i];
          if (min != null) {
            if (f.properties[attribute] < min) {
              min = f.properties[attribute];
            }
          } 
          else {
            min =  f.properties[attribute];
          }

          if (max) {
            if (f.properties[attribute] > max) {
              min = f.properties[attribute];
            }
          }
          else {
              max = f.properties[attribute];
          }
        }
        return [min, max];
      },
    "getFeatureStyle": function(feature) {
            var style = {
                    weight: 2,
                    opacity: 1,
                    color: 'white',
                    dashArray: '3',
                    fillOpacity: 0.7
            };
            if (this.legend_column && feature.properties[this.legend_column]) {
                    style.fillColor = this.getFeatureColor(feature.properties[this.legend_column]);
            }
            else {
                    style.fillColor = "blue";
            }
            return style;
    },
    "getFeatureColor": function(value) {
        var step = (this.max - this.min)/8;
        var color;
        if (value < this.min + 1*step) {
          color = '#800026';
        }
        else if (value < this.min + 2*step) {
          color = '#BD0026';
        }
        else if (value < this.min + 3*step) {
          color = '#E31A1C';
        }
        else if (value < this.min + 4*step) {
          color = '#FC4E2A';
        }
        else if (value < this.min + 5*step) {
          color = '#FD8D3C';
        }
        else if (value < this.min + 6*step) {
          color = '#FEB24C';
        }
        else if (value < this.min + 7*step) {
          color = '#FED976';
        }
        else {
          color = '#FFEDA0';
        }
        return color;
    }
  },
  watch: {
    legend_column: function(name) {
      var mm =  this.getMM(name);
      this.min = mm[0];
      this.max = mm[1];
      for (var i in this.layer._layers) {
        var l = this.layer._layers[i];
        l.setStyle(this.getFeatureStyle(l.feature));
      }
      
    },
    "map": function(map) {
      this.map = map;
      this.layer = L.geoJSON(geojson.features, {
          //onEachFeature: onEachFeature,
          style: this.getFeatureStyle
      }).addTo(map);
    }
  }
});

