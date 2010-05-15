function setupFrontMap(){

    // Setup the map
    oNavigation = new OpenLayers.Control.Navigation();
    oNavigation.zoomWheelEnabled = false;
    oPanZoomBar = new OpenLayers.Control.PanZoomBar();

    oMap = new OpenLayers.Map ("divFrontMap", {
          controls:[
              oNavigation,
              oPanZoomBar,
              new OpenLayers.Control.Attribution()],
          maxExtent: new OpenLayers.Bounds(-20037508.34,-20037508.34,20037508.34,20037508.34),
          maxResolution: 156543.0399,
          numZoomLevels: 10,
          units: 'm',
          projection: new OpenLayers.Projection("EPSG:900913"),
          displayProjection: new OpenLayers.Projection("EPSG:4326")
      } );


     var cloudmade = new OpenLayers.Layer.CloudMade("CloudMade", {
         key: 'f0a3ed3f086e42bbb3691bef27581977',
         styleId: 17368
     });
     oMap.addLayer(cloudmade);
     

      oMarkersLayer = new OpenLayers.Layer.Markers("Markers");
      oMap.addLayer(oMarkersLayer);      

     // Make icon
     var oIconSize = new OpenLayers.Size(21,25);
     var oIconOffset = new OpenLayers.Pixel(-(oIconSize.w/2), -oIconSize.h);
     var oIcon = new OpenLayers.Icon('http://www.openstreetmap.org/openlayers/img/marker.png',oIconSize, oIconOffset);

     var oData = eval('('+ $('#hidMapData').val() + ')');

    for (var i=0; i < oData.length; i++) {

        //get the lat/lng
        iLat = oData[i].lat;
        iLng = oData[i].lng;         
        var oLngLat = new OpenLayers.LonLat(iLng, iLat).transform(new OpenLayers.Projection("EPSG:4326"), oMap.getProjectionObject());         

        //make the marker
        var oMarker = new OpenLayers.Marker(oLngLat,oIcon.clone())
        oMarkersLayer.addMarker(oMarker);

    }
     //zoom to extent of the markers
     oMap.zoomToExtent(oMarkersLayer.getDataExtent());    

}