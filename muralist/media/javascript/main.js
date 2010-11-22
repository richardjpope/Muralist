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
     var oIconSize = new OpenLayers.Size(42,54);
     var oIconOffset = new OpenLayers.Pixel(-(oIconSize.w/2), -oIconSize.h);
     var oIconGood = new OpenLayers.Icon('/site-media/images/brush_good.png',oIconSize, oIconOffset);
      var oIconOK = new OpenLayers.Icon('/site-media/images/brush_ok.png',oIconSize, oIconOffset);
     var oIconThreat = new OpenLayers.Icon('/site-media/images/brush_threat.png',oIconSize, oIconOffset);     
     var oIconLost = new OpenLayers.Icon('/site-media/images/brush_lost.png',oIconSize, oIconOffset);           

     var oData = eval('('+ $('#hidMapData').val() + ')');

    for (var i=0; i < oData.length; i++) {

        //get the lat/lng
        iLat = oData[i].lat;
        iLng = oData[i].lng;         
        var oLngLat = new OpenLayers.LonLat(iLng, iLat).transform(new OpenLayers.Projection("EPSG:4326"), oMap.getProjectionObject());         

        //make the marker
        oIconAdd = null
        if(oData[i].condition_tag == 'lost'){
          oIconAdd = oIconLost.clone();
        }else if (oData[i].condition_tag == 'good'){
          oIconAdd = oIconGood.clone();            
        }else if (oData[i].condition_tag == 'threat'){
          oIconAdd = oIconThreat.clone();
        }else{
          oIconAdd = oIconOK.clone();            
        }
        
        var oMarker = new OpenLayers.Marker(oLngLat,oIconAdd)
        oMarker.html = '<a href="/murals/' + oData[i].uri_slug + '/">' + oData[i].title + '</a>';
        oMarker.events.register("mousedown", oMarker,
                function(o, b){
                    var oPopup = new OpenLayers.Popup.AnchoredBubble("item", this.lonlat, 
                        new OpenLayers.Size(160, 60), this.html, this.icon, true);
                    oMap.addPopup(oPopup, true);
                }  
        );
        oMarker.events.register("mouseover", oMarker,
                function(o, b){
                    document.getElementById('divFrontMap').style.cursor='pointer';
                }  
        );
        oMarker.events.register("mouseout", oMarker,
                function(o, b){
                    document.getElementById('divFrontMap').style.cursor='auto';
                }  
        );

        
        oMarkersLayer.addMarker(oMarker);

    }
     //zoom to extent of the markers
     oMap.zoomToExtent(oMarkersLayer.getDataExtent());    

}