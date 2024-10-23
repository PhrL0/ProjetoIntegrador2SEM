// Gráfico Donut (inicia zerado)
var optionsDonut = {
    series: [0, 0, 0],
    labels: ['Tênis', 'Sandália', 'Chinelo'],
    chart: {
        type: 'donut',
        width: 300,
        height: 300
    },
    responsive: [{
        breakpoint: 480,
        options: {
            chart: {
                width: 200
            },
            legend: {
                position: 'bottom'
            }
        }
    }]
};
var chartDonut = new ApexCharts(document.querySelector("#chart-donut"), optionsDonut);
chartDonut.render();

navigator.mediaDevices.getUserMedia({ video: true })
    .then(function(stream) {
        // Código para lidar com a câmera funcionando
        let video = document.querySelector('video');
        video.srcObject = stream;
    })
    .catch(function(err) {
        console.log("Erro ao acessar a câmera: " + err);
    });


// Gráfico de Linhas (inicia zerado e com eixo X sendo segundos)
var optionsLine = {
    series: [{
        name: "Tênis",
        data: Array(12).fill(0) // Inicia com 12 valores zerados
    }, {
        name: "Sandália",
        data: Array(12).fill(0) // Inicia com 12 valores zerados
    }, {
        name: "Chinelo",
        data: Array(12).fill(0) // Inicia com 12 valores zerados
    }],
    chart: {
        height: 350,
        type: 'line',
        animations: {
            enabled: true,
            easing: 'easeout',
            speed: 800
        },
        zoom: {
            enabled: false
        }
    },
    stroke: {
        curve: 'smooth'
    },
    xaxis: {
        categories: Array.from({ length: 12 }, (_, i) => `${i + 1}s`) // Mostra 12 segundos no eixo X
    }
};
var chartLine = new ApexCharts(document.querySelector("#chart-line"), optionsLine);
chartLine.render();

// Função para gerar valores aleatórios
function getRandomData(length) {
    return Array.from({ length }, () => Math.floor(Math.random() * 100));
}

// Gráficos Sparkline (representam cada categoria de sapato)
var spark1 = {
    chart: {
        id: 'spark1',
        group: 'sparks',
        type: 'line',
        height: 80,
        sparkline: {
            enabled: true
        }
    },
    series: [{
        data: Array(12).fill(0) // Inicia zerado
    }],
    stroke: {
        curve: 'smooth'
    },
    markers: {
        size: 0
    },
    grid: {
        padding: {
            top: 20,
            bottom: 10,
            left: 10
        }
    },
    colors: ['#fff'],
    tooltip: {
        x: {
            show: false
        },
        y: {
            title: {
                formatter: function formatter(val) {
                    return '';
                }
            }
        }
    }
};

var spark2 = {
    chart: {
        id: 'spark2',
        group: 'sparks',
        type: 'line',
        height: 80,
        sparkline: {
            enabled: true
        }
    },
    series: [{
        data: Array(12).fill(0) // Inicia zerado
    }],
    stroke: {
        curve: 'smooth'
    },
    markers: {
        size: 0
    },
    grid: {
        padding: {
            top: 20,
            bottom: 10,
            left: 10
        }
    },
    colors: ['#fff'],
    tooltip: {
        x: {
            show: false
        },
        y: {
            title: {
                formatter: function formatter(val) {
                    return '';
                }
            }
        }
    }
};

var spark3 = {
    chart: {
        id: 'spark3',
        group: 'sparks',
        type: 'line',
        height: 80,
        sparkline: {
            enabled: true
        }
    },
    series: [{
        data: Array(12).fill(0) // Inicia zerado
    }],
    stroke: {
        curve: 'smooth'
    },
    markers: {
        size: 0
    },
    grid: {
        padding: {
            top: 20,
            bottom: 10,
            left: 10
        }
    },
    colors: ['#fff'],
    tooltip: {
        x: {
            show: false
        },
        y: {
            title: {
                formatter: function formatter(val) {
                    return '';
                }
            }
        }
    }
};

// Renderiza os Sparklines
new ApexCharts(document.querySelector("#spark1"), spark1).render();
new ApexCharts(document.querySelector("#spark2"), spark2).render();
new ApexCharts(document.querySelector("#spark3"), spark3).render();

// Função para atualizar o gráfico Donut com valores aleatórios
function updateDonutChart() {
    const newSeries = getRandomData(3); // 3 valores aleatórios para o donut
    chartDonut.updateSeries(newSeries);
}

// Função para atualizar o gráfico de Linhas com valores aleatórios
function updateLineChart() {
    const newSeries = [
        { name: "Tênis", data: getRandomData(12) },
        { name: "Sandália", data: getRandomData(12) },
        { name: "Chinelo", data: getRandomData(12) }
    ];
    chartLine.updateSeries(newSeries);

    // Atualiza as categorias (segundos) no eixo X
    const newCategories = Array.from({ length: 12 }, (_, i) => `${i + 1}s`);
    chartLine.updateOptions({
        xaxis: {
            categories: newCategories
        }
    });

    // Atualiza os gráficos Sparkline com os mesmos dados das categorias correspondentes
    ApexCharts.exec('spark1', 'updateSeries', [{ data: newSeries[0].data }]); // Tênis
    ApexCharts.exec('spark2', 'updateSeries', [{ data: newSeries[1].data }]); // Sandália
    ApexCharts.exec('spark3', 'updateSeries', [{ data: newSeries[2].data }]); // Chinelo
}

// Função para atualizar todos os gráficos
function updateAllCharts() {
    updateDonutChart();
    updateLineChart();
}

// Atualiza os gráficos a cada 1 segundo
setInterval(updateAllCharts, 1000);
