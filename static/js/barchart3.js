chartxy()

function chartxy() {
    var ctx = document.getElementById("chartxy").getContext('2d');

    dataset = $.ajax({
        type: "POST",
        url: "/ajax/statistics/index",
        async: false,

        success: function(data, textStatus, jqXHR) {

        },

        error: function(jqXHR, textStatus, errorThrown) {

        },

        complete: function() {

        }
    });

    console.log(dataset)

    var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [
        {
            label: dataset[0]['class'],
            data: dataset[0]['points'],
            backgroundColor: [
                'rgba(54, 162, 235, 0.2)'
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)'
            ],
            borderWidth: 1
        },
        {
            label: dataset[1]['class'],
            data: dataset[1]['points'],
            backgroundColor: [
                'rgba(75, 192, 192, 0.2)'
            ],
            borderColor: [
                'rgba(75, 192, 192, 1)'
            ],
            borderWidth: 1
        },
        {
            label: dataset[1]['class'],
            data: dataset[1]['points'],
            backgroundColor: [

                'rgba(255, 159, 64, 0.2)'
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

setInterval(function get_data(){
    chartxy()
}, 10000);