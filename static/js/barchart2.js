diagram()

function diagram() {
    var ctx = document.getElementById("chartab").getContext('2d');

    dataset = $.ajax({
        type: "POST",
        url: "/ajax/statistics/index",
        async: false,

        success: function(data, textStatus, jqXHR) {
                console.log('yeah')
        },

        error: function(jqXHR, textStatus, errorThrown) {
                console.log('noooo')
        },

        complete: function() {
            console.log('finished')
        }
    });

    console.log(dataset)

    var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [
        {
            label: 'Schüler xa',
            data: [12],
            backgroundColor: [
                'rgba(54, 162, 235, 0.2)'
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)'
            ],
            borderWidth: 1
        },
        {
            label: 'Schüler ab',
            data: [8],
            backgroundColor: [
                'rgba(75, 192, 192, 0.2)'
            ],
            borderColor: [
                'rgba(75, 192, 192, 1)'
            ],
            borderWidth: 1
        },
        {
            label: 'Schüler xy',
            data: [19],
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
    diagram()
}, 10000);