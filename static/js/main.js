$(document).ready(function(){

    var errorClass = 'error';
    var mutedClass = 'muted';

    $("#zipcodeSubmit").click(function(e){
        e.preventDefault();
        var zipcode = $("#inputZipcode").val();
        var isnum = /^\d+$/.test(zipcode);
        if(zipcode.length == 5 && isnum){
            /* Clean up */
            $("#registrationoffice-id").children().remove();
            $("#municipality-id").children().remove();
            $("#municipality").fadeOut();
            $("#municipality").siblings("legend").addClass(mutedClass);
            $("#registrationOffice").fadeOut();
            $("#registrationOffice").siblings("legend").addClass(mutedClass);
            $("#address").fadeOut();
            $("#address").siblings("legend").addClass(mutedClass);
            $("#inputZipcode").parents("div[class='control-group error']").removeClass(errorClass);
            $("#zipcodeInfo").fadeOut();
            $("#zipcodeError").fadeOut();

            /*  */
            $.getJSON("/api/v1/zipcode/?format=json&zipcode="+ zipcode,
                function(data){
                    if(data.meta.total_count > 0){
                        var registrationoffices = data.objects[0].registrationoffices;
                        var municipalities = data.objects[0].municipalities;



                        if(registrationoffices.length > 0){
                            $.each(registrationoffices, function() {
                                $("#registrationoffice-id")
                                 .append($("<option></option>")
                                 .attr("value",this.id)
                                 .text(this.name));
                            });
                            $("#registrationOffice").fadeIn();
                            $("#registrationOffice").siblings("legend").removeClass(mutedClass);
                        } else {

                            $.each(municipalities, function() {
                                $("#municipality-id")
                                 .append($("<option></option>")
                                 .attr("value",this.id)
                                 .text(this.name));
                            });
                            $("#municipality").fadeIn();
                            $("#municipality").siblings("legend").removeClass(mutedClass);
                        }
                    } else {
                        $("#zipcodeInfo").fadeIn();
                    }
                }
            );
        } else {
            $("#inputZipcode").parents("div[class='control-group']").addClass(errorClass);
            $("#municipality").fadeOut();
            $("#municipality").siblings("legend").addClass(mutedClass);
            $("#registrationOffice").fadeOut();
            $("#registrationOffice").siblings("legend").addClass(mutedClass);
            $("#address").fadeOut();
            $("#address").siblings("legend").addClass(mutedClass);
            $("#zipcodeInfo").fadeOut();
            $("#zipcodeError").fadeIn();
        }
    });

    $("#municipalitySubmit").click(function(e){
        e.preventDefault();
        $("#address").fadeIn();
        $("#address").siblings("legend").removeClass(mutedClass);
    });

    $("#registrationOfficeSubmit").click(function(e){
        e.preventDefault();
        $("#address").fadeIn();
        $("#address").siblings("legend").removeClass(mutedClass);
    });
});


/* Piwik */
var _paq = _paq || [];
_paq.push(["setDoNotTrack", true]);
_paq.push(["trackPageView"]);
_paq.push(["enableLinkTracking"]);

(function() {
var u=(("https:" == document.location.protocol) ? "https" : "http") + "://jbr.norma.uberspace.de/piwik/";
_paq.push(["setTrackerUrl", u+"piwik.php"]);
_paq.push(["setSiteId", "2"]);
var d=document, g=d.createElement("script"), s=d.getElementsByTagName("script")[0]; g.type="text/javascript";
g.defer=true; g.async=true; g.src=u+"piwik.js"; s.parentNode.insertBefore(g,s);
})();
