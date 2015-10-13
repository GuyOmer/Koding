$(document).ready(function() {
    
    // load data via ajax when form is submitted
    $('form[name=quote-form]').submit(function() {
        
        // determine symbol
        var symbol = $('input[name=symbol]').val();
    
        // send request to quote.php
        $.ajax({
                url: 'quote2.php',
                type: 'POST',
                dataType:'JSON',
                data: {
                    symbol: symbol
                      },
                success: function(response) {
                    if(response.status == "bad") {
                        parsed = "<strong>Nothing was found!</strong>"
                        $('.form-group').addClass(" has-error");
                    }
                    else {
                    parsed = "<table id=\"quote-result\" class=\"table table-striped\">" +
                             "<thead>" +
                             "<tr>" +
                                 "<th class=\"col-md-1\">Symbol</th>" +
                                 "<th class=\"col-md-2\">Name</th>" +
                                 "<th class=\"col-md-1\">Price</th>" +
                             "</tr>" +
                             "</thead>" +
                             "<tbody>" +
                             "<tr>" +
                                 "<td class=\"col-md-1\">" + response.symbol + "</td>" +
                                 "<td class=\"col-md-2\">" + response.name + "</td>" +
                                 "<td class=\"col-md-1\">" + response.price + "</td>" +
                             "</tr>" +
                             "</tbody>" +
                             "</table>" +
                             "<div class=\"container\">" +
                                 "<a href=\"quote.php\">Back</a>" +
                             "</div>";
                    $('.form-group').removeClass(" has-error");
                    }
                    $('#result').html("").html(parsed);
                    setTimeout(function(){
                    $(".btn").removeClass("btn-success").addClass("btn-primary");}
                    , 1000);
                }
            });
         // since we're overridding form submission, make sure it doesn't submit       
        return false;
    });
});