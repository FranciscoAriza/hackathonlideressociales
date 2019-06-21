var MILLS_TO_IGNORE_SEARCH = 500;

var MILLS_TO_IGNORE_LIKES = 500;

$(document).ready(function()  {

  load_bitacora();

  // $(document).ready(_.debounce(myeventsSearch,
  //     MILLS_TO_IGNORE_SEARCH, true));
  //
  // $('#username').change(_.debounce(myeventsSearch,
  //     MILLS_TO_IGNORE_SEARCH, true));
  //
  // $('#listar_mis_eventos').click(_.debounce(myeventsSearch,
  //     MILLS_TO_IGNORE_SEARCH, true));
  $('#load_bitacora').click(load_bitacora);
  $('#load_profile').click(load_profile);
  $('#load_estado_salud').click(load_estado_salud);
  //     MILLS_TO_IGNORE_SEARCH, true));

});
