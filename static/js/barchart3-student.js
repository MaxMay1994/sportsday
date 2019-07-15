chartxy()

setInterval(function get_data_2(){
    chartxy()
}, 10000);

function chartxy() {
    var ctx = document.getElementById("chartxy").getContext('2d');

    var str = window.location.pathname;
    var res = str.substring(6, 11);

    dataset = $.ajax({
        type: "POST",
        url: "/ajax/statistics/student/class/" + res,
        async: false,

        success: function(data, textStatus, jqXHR) {
        },

        error: function(jqXHR, textStatus, errorThrown) {
        },

        complete: function() {
        }
    });

    var jsonObj = $.parseJSON(dataset.responseText);

    var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [
        {
            label: 'Du',
            data: [jsonObj[0]['points']],
            backgroundColor: [
                'rgba(54, 162, 235, 0.5)'
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)'
            ],
            borderWidth: 1
        },
        {
            label: jsonObj[1]['studentnumber'],
            data: [jsonObj[1]['points']],
            backgroundColor: [
                'rgba(255, 159, 64, 0.5)'
            ],
            borderColor: [
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        },
        {
            label: jsonObj[2]['studentnumber'],
            data: [jsonObj[2]['points']],
            backgroundColor: [

                'rgba(255, 159, 64, 0.5)'
            ],
            borderColor: [
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        },
        {
            label: jsonObj[3]['studentnumber'],
            data: [jsonObj[3]['points']],
            backgroundColor: [

                'rgba(255, 159, 64, 0.5)'
            ],
            borderColor: [
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }

        ]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        },
        responsive: true
    }
});
}