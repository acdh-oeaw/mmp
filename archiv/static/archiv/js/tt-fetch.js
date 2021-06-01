async function get_time_table_json() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if(this.readyState == 4 && this.status == 200) {
        var data = JSON.parse(xhttp.responseText);
        var tbody = '<tbody>';
        for(var i = 0; i < data.length; i++) {
          var row = '<tr>';
          row += `<td>${data[i].start_date}</td>`;
          row += `<td>${data[i].end_date}</td>`;
          row += `<td><a href="${ data[i].ent_detail_view }">${data[i].ent_title}</a></td>`;
          row += `<td>${data[i].ent_description}</td>`;
          row += `<td>${data[i].ent_type}</td></tr>`;
          tbody += row;
        }
        tbody += '</tbody>';
        var table = `<table class="table table-striped">
                      <thead>
                        <tr>
                          <th>Start-date</th>
                          <th>End-date</th>
                          <th>Title</th>
                          <th>Description</th>
                          <th>Type</th>
                        </tr>  
                      </thead>
                      ${tbody}
                    </table>`
        document.getElementById('time_table').innerHTML = table;
        }
      };
    var url = document.getElementById('time_table').getAttribute('data-target');
    xhttp.open('GET', url, true);  
    xhttp.setRequestHeader("Content-type", "application/json");   
    xhttp.send();
};