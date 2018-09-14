// Call the dataTables jQuery plugin
$(document).ready(function() {
 $('#dataTable').DataTable();
});


$(document).ready(function() {
var incomingtable = $('#incomingTable').DataTable({ ajax : '/ajax/ajax_incoming' });

setInterval( function () {
    incomingtable.ajax.reload();
}, 3000 );

});


$(document).ready(function() {
var logstable = $('#logsTable').DataTable({ ajax : '/ajax/ajax_logs' });

  setInterval( function () {
    logstable.ajax.reload();
}, 3000 );

});


$(document).ready(function() {
var missedtable = $('#missedTable').DataTable({ ajax : '/ajax/ajax_missed' });

  setInterval( function () {
    missedtable.ajax.reload();
}, 3000 );

});

$(document).ready(function() {
var todaytable = $('#todayTable').DataTable({ ajax : '/ajax/ajax_today' });

  setInterval( function () {
    todaytable.ajax.reload();
}, 3000 );

});

$(document).ready(function() {
var currenttable = $('#currentTable').DataTable({ ajax : '/ajax/ajax_current' });

  setInterval( function () {
    currenttable.ajax.reload();
}, 3000 );

});

$(document).ready(function() {
var voicemailtable = $('#voicemailTable').DataTable({ ajax : '/ajax/ajax_voicemail' });

  setInterval( function () {
    voicemailtable.ajax.reload();
}, 3000 );

});

$(document).ready(function() {
var outgoingtable = $('#outgoingTable').DataTable({ ajax : '/ajax/ajax_outgoing' });

  setInterval( function () {
    outgoingtable.ajax.reload();
}, 3000 );

});
