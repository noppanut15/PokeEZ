var map, heatmap;

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 3,
    center: {lat: 35.676315, lng: -80.939015},
    mapTypeId: 'terrain'
  });

  heatmap = new google.maps.visualization.HeatmapLayer({
    data: getPoints(),
    map: map,
    radius: 20
  });

/*  var markers = getPoints();
  var bounds = new google.maps.LatLngBounds();
  for (var i = 0; i < markers.length; i++) {
      bounds.extend(markers[i]);
  }

  map.fitBounds(bounds);*/
}

function getPoints() {

    var json = (function () { 
          var json = null; 
          $.ajax({ 
              'async': false, 
              'global': false, 
              'url': poke_map_json, 
              'dataType': "json", 
              'success': function (data) {
                   json = data; 
               }
          });
          return json;
      })();

    contents = []
    for (var i = 0, length = json.length; i < length; i++) {
          var data = json[i];
          contents.push(new google.maps.LatLng(data.lat, data.lng));
    }
    return contents
}
