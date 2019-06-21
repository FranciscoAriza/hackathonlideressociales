var load_bitacora = function()  {
  var username = $('#username').val().trim();

  if(username.length < 3)  {
    //Too short. Ignore the submission, and erase any current results.
    $('#contenido').html("");

  }  else  {
    //There are at least two characters. Execute the search.

    var processServerResponse = function(sersverResponse_data, textStatus_ignored,
                        jqXHR_ignored)  {
      //alert("sersverResponse_data='" + sersverResponse_data + "', textStatus_ignored='" + textStatus_ignored + "', jqXHR_ignored='" + jqXHR_ignored + "'");
      $('#contenido').html(sersverResponse_data);
    }

    var config = {
      /*
        Using GET allows you to directly call the search page in
        the browser:
        http://the.url/search/?color_search_text=bl
        Also, GET-s do not require the csrf_token
       */
      type: "GET",
      url: LOAD_MY_TIMELINE_URL,
      data: {
        'username' : username,
      },
      dataType: 'html',
      success: processServerResponse
    };
    $.ajax(config);
  }
};


var load_profile = function()  {
  var username = $('#username').val().trim();

  if(username.length < 3)  {
    //Too short. Ignore the submission, and erase any current results.
    $('#contenido').html("");

  }  else  {
    //There are at least two characters. Execute the search.

    var processServerResponse = function(sersverResponse_data, textStatus_ignored,
                        jqXHR_ignored)  {
      //alert("sersverResponse_data='" + sersverResponse_data + "', textStatus_ignored='" + textStatus_ignored + "', jqXHR_ignored='" + jqXHR_ignored + "'");
      $('#contenido').html(sersverResponse_data);
    }

    var config = {
      /*
        Using GET allows you to directly call the search page in
        the browser:
        http://the.url/search/?color_search_text=bl
        Also, GET-s do not require the csrf_token
       */
      type: "GET",
      url: LOAD_MY_PROFILE_URL,
      data: {
        'username' : username,
      },
      dataType: 'html',
      success: processServerResponse
    };
    $.ajax(config);
  }
};

var load_estado_salud = function()  {
  var username = $('#username').val().trim();

  if(username.length < 3)  {
    //Too short. Ignore the submission, and erase any current results.
    $('#contenido').html("");

  }  else  {
    //There are at least two characters. Execute the search.

    var processServerResponse = function(sersverResponse_data, textStatus_ignored,
                        jqXHR_ignored)  {
      //alert("sersverResponse_data='" + sersverResponse_data + "', textStatus_ignored='" + textStatus_ignored + "', jqXHR_ignored='" + jqXHR_ignored + "'");
      $('#contenido').html(sersverResponse_data);
    }

    var config = {
      /*
        Using GET allows you to directly call the search page in
        the browser:
        http://the.url/search/?color_search_text=bl
        Also, GET-s do not require the csrf_token
       */
      type: "GET",
      url: LOAD_MY_ESTADO_SALUD_URL,
      data: {
        'username' : username,
      },
      dataType: 'html',
      success: processServerResponse
    };
    $.ajax(config);
  }
};
