// Call the dataTables jQuery plugin
$(document).ready(function() {
 $('#dataTable').DataTable();
});


$(document).ready(function() {
var incomingtable = $('#incomingTable').DataTable({ ajax : 'call_logs/ajax/ajax_incoming' });

setInterval( function () {
    incomingtable.ajax.reload();
}, 3000 );

});


$(document).ready(function() {
var logstable = $('#logsTable').DataTable({ ajax : 'call_logs/ajax/ajax_logs' });

  setInterval( function () {
    logstable.ajax.reload();
}, 3000 );

});


$(document).ready(function() {
var missedtable = $('#missedTable').DataTable({ ajax : 'call_logs/ajax/ajax_missed' });

  setInterval( function () {
    missedtable.ajax.reload();
}, 3000 );

});
