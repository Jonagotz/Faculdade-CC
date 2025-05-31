$(document).ready(function() {
    function toggleTheme() {
        $("body").toggleClass("dark-theme");
        $("body").toggleClass("light-theme");
    }

    function mudarTexto(curso) { 
        if (curso === 'ciencia') {
          $('#titulo').text("Ciência da Computação");
          $('.descricao-turno').text("Vespertino e Noturno.");
          $('.descricao-duracao').text("Matutino: 8 semestres, Noturno: 10 semestres.\n");
          $('.descricao-coordenacao').text("Braulio Adriano de Mello.\n");
          $('.descricao-sobre').text("O curso de Ciência da Computação abrange desde a lógica de programação até a construção de sistemas. Durante o programa, os alunos aprendem a utilizar diferentes linguagens computacionais para a criação de sistemas, como C, C++, Java, Python, entre outras.\n");
        } else if (curso === 'historia') {
            $('#titulo').text("História");
            $('.descricao-turno').text("Noturno e vespertino\n");
            $('.descricao-duracao').text("Matutino: 8 semestres, Noturno: 10 semestres.\n");
            $('.descricao-coordenacao').text("Luciana Menezes.\n");
            $('.descricao-sobre').text("O curso de História abrange um campo de estudo que envolve a narração sistemática de eventos passados, geralmente relacionados a seres humanos e às sociedades que eles formaram ao longo do tempo. Ela busca compreender e interpretar os eventos do passado, examinando suas causas, efeitos, contextos e significados.\n");
        } else if (curso === 'geografia') {
            $('#titulo').text("Geografia");
            $('.descricao-turno').text("Noturno e vespertino.\n");
            $('.descricao-duracao').text("Matutino: 8 semestres, Noturno: 10 semestres.\n");
            $('.descricao-coordenacao').text("Roberto Cavalcanti.\n");
            $('.descricao-sobre').text("O curso universitário de Geografia é uma graduação de nível superior que dura em média quatro anos. A grade curricular do curso é composta por disciplinas teóricas e práticas, que abordam uma ampla gama de temas como: Geografia física: Estudo dos fenômenos físicos da Terra, como clima, relevo, vegetação e hidrografia.\n");
        }
    }

    $("#theme-button").on("click", toggleTheme);

    $(".label-curso").on("click", function() {
        let curso = $(this).attr("for");
        mudarTexto(curso);
    });

});