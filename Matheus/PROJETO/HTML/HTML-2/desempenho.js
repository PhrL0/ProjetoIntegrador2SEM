    // Gráfico Donut
    var optionsDonut = {
        series: [44, 55, 41],
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

    // Gráfico de Linhas
    var optionsLine = {
        series: [{
            name: "Session Duration",
            data: [45, 52, 38, 24, 33, 26, 21, 20, 6, 8, 15, 10]
        }],
        chart: {
            height: 350,
            type: 'line',
            zoom: {
                enabled: false
            }
        },
        xaxis: {
            categories: ['01 Jan', '02 Jan', '03 Jan', '04 Jan', '05 Jan', '06 Jan', '07 Jan', '08 Jan', '09 Jan', '10 Jan', '11 Jan', '12 Jan']
        }
    };
    var chartLine = new ApexCharts(document.querySelector("#chart-line"), optionsLine);
    chartLine.render();

    // WebSocket para atualizar gráficos
    let values = [];
    let ws = new WebSocket('ws://127.0.0.1:1880/ws/data');
    ws.onmessage = function (event) {
        let receivedData = JSON.parse(event.data);
        let contador = receivedData.Contador1;

        // Adiciona o novo valor ao array de valores
        values.push(contador);

        // Limita o array de valores a 10 itens
        if (values.length > 10) values.shift();

        // Calcula a mediana e atualiza o gráfico Donut
        const median = values.sort((a, b) => a - b)[Math.floor(values.length / 2)];
        chartDonut.updateSeries([median, 55, 41]);

        // Atualiza o gráfico de linhas com os dados recebidos
        chartLine.updateSeries([{
            data: values
        }]);
    };

    // Gráficos Sparkline
    var spark1 = {
        chart: {
            id: 'spark1',
            group: 'sparks',
            type: 'line',
            height: 80,
            sparkline: {
                enabled: true
            },
            dropShadow: {
                enabled: true,
                top: 1,
                left: 1,
                blur: 2,
                opacity: 0.2,
            }
        },
        series: [{
            data: [25, 66, 41, 59, 25, 44, 12, 36, 9, 21]
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
                left: 110
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
    }

    var spark2 = {
        chart: {
            id: 'spark2',
            group: 'sparks',
            type: 'line',
            height: 80,
            sparkline: {
                enabled: true
            },
            dropShadow: {
                enabled: true,
                top: 1,
                left: 1,
                blur: 2,
                opacity: 0.2,
            }
        },
        series: [{
            data: [12, 14, 2, 47, 32, 44, 14, 55, 41, 69]
        }],
        stroke: {
            curve: 'smooth'
        },
        grid: {
            padding: {
                top: 20,
                bottom: 10,
                left: 110
            }
        },
        markers: {
            size: 0
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
    }

    var spark3 = {
        chart: {
            id: 'spark3',
            group: 'sparks',
            type: 'line',
            height: 80,
            sparkline: {
                enabled: true
            },
            dropShadow: {
                enabled: true,
                top: 1,
                left: 1,
                blur: 2,
                opacity: 0.2,
            }
        },
        series: [{
            data: [47, 45, 74, 32, 56, 31, 44, 33, 45, 19]
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
                left: 110
            }
        },
        colors: ['#fff'],
        xaxis: {
            crosshairs: {
                width: 1
            },
        },
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
    }

    var spark4 = {
        chart: {
            id: 'spark4',
            group: 'sparks',
            type: 'line',
            height: 80,
            sparkline: {
                enabled: true
            },
            dropShadow: {
                enabled: true,
                top: 1,
                left: 1,
                blur: 2,
                opacity: 0.2,
            }
        },
        series: [{
            data: [15, 75, 47, 65, 14, 32, 19, 54, 44, 61]
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
                left: 110
            }
        },
        colors: ['#fff'],
        xaxis: {
            crosshairs: {
                width: 1
            },
        },
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
    }

    new ApexCharts(document.querySelector("#spark1"), spark1).render();
    new ApexCharts(document.querySelector("#spark2"), spark2).render();
    new ApexCharts(document.querySelector("#spark3"), spark3).render();
    new ApexCharts(document.querySelector("#spark4"), spark4).render();