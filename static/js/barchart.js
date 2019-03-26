diagram()

function diagram() {
    var ctx = document.getElementById("myChart").getContext('2d');

    dataset = $.ajax({
        type: "POST",
        url: "/ajax/statistics/index/class",
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
            label: jsonObj[0]['classname'],
            data: [jsonObj[0]['points']],
            backgroundColor: [
                'rgba(54, 162, 235, 0.2)'
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)'
            ],
            borderWidth: 1
        },
        {
            label: jsonObj[1]['classname'],
            data: [jsonObj[1]['points']],
            backgroundColor: [
                'rgba(75, 192, 192, 0.2)'
            ],
            borderColor: [
                'rgba(75, 192, 192, 1)'
            ],
            borderWidth: 1
        },
        {
            label: jsonObj[2]['classname'],
            data: [jsonObj[2]['points']],
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