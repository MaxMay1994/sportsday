chartxy()

setInterval(function get_data_2(){
    chartxy()
}, 10000);

function chartxy() {
    var ctx = document.getElementById("chartxy").getContext('2d');

    dataset = $.ajax({
        type: "POST",
        url: "/ajax/statistics/index/student",
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
            label: jsonObj[0]['studentnumber'],
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
                'rgba(75, 192, 192, 0.5)'
            ],
            borderColor: [
                'rgba(75, 192, 192, 1)'
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