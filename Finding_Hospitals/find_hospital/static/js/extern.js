var lat
var lng
function initMap() {
  var place 
   var map = new google.maps.Map(document.getElementById('map'), {
     center: {lat: 0, lng: 0},
    zoom: 2 
  }); 
  var card = document.getElementById('pac-card');
  var input = document.getElementById('pac-input');

  map.controls[google.maps.ControlPosition.TOP_RIGHT].push(card);

  var autocomplete = new google.maps.places.Autocomplete(input);

  // Bind the map's bounds (viewport) property to the autocomplete object,
  // so that the autocomplete requests use the current map bounds for the
  // bounds option in the request.
  autocomplete.bindTo('bounds', map);

  // Set the data fields to return when the user selects a place.
  autocomplete.setFields(
      ['address_components', 'geometry', 'icon', 'name']);

  var infowindow = new google.maps.InfoWindow();
  var infowindowContent = document.getElementById('infowindow-content');
  infowindow.setContent(infowindowContent);
  var marker = new google.maps.Marker({
    map: map,
    anchorPoint: new google.maps.Point(0, -29)
  });

  autocomplete.addListener('place_changed', function() {
    infowindow.close();
    marker.setVisible(false);
    place = autocomplete.getPlace();
    if (!place.geometry) {
      // User entered the name of a Place that was not suggested and
      // pressed the Enter key, or the Place Details request failed.
      window.alert("No details available for input: '" + place.name + "'");
      return;
    }
    //document.getElementById('pac-input').value = place
    // If the place has a geometry, then present it on a map.
      lat = place.geometry['location'].lat();
      lng = place.geometry['location'].lng();  
      // resp = updateLatLng(lat, lng);
      console.log(place.geometry['location'].lat());
      console.log(place.geometry['location'].lng());

        
    if (place.geometry.viewport) {
      map.fitBounds(place.geometry.viewport);
    } else {
      map.setCenter(place.geometry.location);

      

      map.setZoom(10);  // Why 17? Because it looks good.
    }
    marker.setPosition(place.geometry.location);
    marker.setVisible(true);

    var address = '';
    if (place.address_components) {
      address = [
        (place.address_components[0] && place.address_components[0].short_name || ''),
        (place.address_components[1] && place.address_components[1].short_name || ''),
        (place.address_components[2] && place.address_components[2].short_name || '')
      ].join(' ');
    }

    infowindowContent.children['place-icon'].src = place.icon;
    infowindowContent.children['place-name'].textContent = place.name;
    infowindowContent.children['place-address'].textContent = address;
    infowindow.open(map, marker);
  });


 //console.log(place)
}

function updateLatLng(lat, lng) {
    var data = {'lati': lat, 'long': lng, csrfmiddlewaretoken: '{{ csrf_token }}'};
    $.post('{% url "results" %}', data);
    console.log(lat);
      console.log(lng);
    var response = '{{result}}';
    return response
};

//     function csrfSafeMethod(method) {
//         // these HTTP methods do not require CSRF protection
//         return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
//       }

//       $.ajaxSetup({
//         beforeSend: function(xhr, settings) {
//           if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//             xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
//           }
//         }
//       });
//       if (lat&&lng) {
//       function now(position) {
//             console.log('Position has been set successfully');
            
// dataToSend = {
//               "fbpost": $("input[name=fb-post]").is(':checked'),
//               "latitude": lat,
//               "longitude": lng
//             };

//             $.ajax({
//               type: "POST",
//               dataType: 'json',
//               url: "{% url 'index' %}",
//               data: JSON.stringify(dataToSend),
//               success: function (msg) {
//                 console.log('Succeeded!');            
//               },
//               error: function (err) {
//                 console.log('Error!');
//               }
//             });
//           }, function (error) {
//               console.log('Position could not be obtained.')
//           };
// }

