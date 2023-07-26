$(document).ready(function (){
    form_actions();
    next_page_button();
    /*window.Scrollbar.init(document.querySelector('#page-1'), {
        damping: 0.2,
    });*/

    var formData = $(this).serialize(); // Serialize form data


    M.updateTextFields();
});

function next_page_button() {
    $('.next-page').on('click', function () {
        let this_page = parseInt($(this).attr('data-this-page'));
        if(
            this_page !== 2 ||
            (this_page === 2 && $('#height').val())
        ) {
            let next_page = parseInt($(this).attr('data-next-page'));
            let this_page_element = $('#page-'+this_page);
            let next_page_element = $('#page-'+next_page);
            if(next_page !== 1) {
                window.Scrollbar.init(document.querySelector('#page-'+next_page), {
                    damping: 0.2,
                });
            }
            if(next_page_element.length > 0) {
                M.updateTextFields();
                this_page_element.removeClass('show-flipped').addClass('exit-flipped');
                setTimeout(function () {
                    this_page_element.hide();
                    next_page_element.addClass('show-flipped').show();
                }, 800);
            }

            switch (this_page) {
                case 2:
                    $('#general-health').hide();
                    setTimeout(function () {
                        $('#general-health').show();
                    }, 1200);
                    break;
                case 3:
                    calculate_risk();
                    break;
            }
        }
    });
}

function form_actions() {
    // page 2
    $('#select-gender .gender').on('click', function () {
        $('#select-gender .gender').removeClass('active');
        $(this).addClass('active');
    });

    $('#height').on('change', function () {
        let value = $(this).val();
        let reg = new RegExp('^\\d+$');
        let flag = false;
        if(reg.test(value)) {
            value = parseInt(value);
            if(value < 20 || value > 230) {
                flag = true;
                toastMSG('Height should be between 20 and 230', 'orange');
            }
        } else {
            flag = true;
            toastMSG('Enter a Valid Value', 'orange');
        }

        if(flag) {
            $(this).val('');
            M.updateTextFields();
        }
    });

    $('.box .buttons-wrapper button.add, .box .buttons-wrapper button.minus').on('click', function () {
        let counter_el = $(this).parent().parent().find('.counter');
        let btn_type = $(this).hasClass('add');
        let value = parseInt(counter_el.attr('data-value'));
        let type = counter_el.attr('id');

        let max = 0;
        let min = 0;
        let suffix = '';
        switch (type) {
            case 'age':
                max = 120;
                min = 1;
                break;

            case 'weight':
                max = 120;
                min = 1;
                suffix = ' KG';
                break;

            case 'physical-health':
            case 'mental-health':
                max = 30;
                min = 0;
                suffix = ' Days';
                break;
        }

        if(btn_type) {
            $(this).parent().find('.minus').prop('disabled', false);
            value++;
            if(value >= max) $(this).prop('disabled', true);
        } else {
            $(this).parent().find('.add').prop('disabled', false);
            value--;
            if(value <= min) $(this).prop('disabled', true);
        }
        counter_el.attr('data-value', value);
        counter_el.text(value + suffix);
    });

    // page 3
    $('.radio-buttons-behavior button').on('click', function () {
        if(!$(this).hasClass('active')){
            $(this).parent().parent().find('button').toggleClass('active').toggleClass('inactive');
        }
    });
}

function calculate_risk() {
    let risk = random_int(1, 100);
    let duration = (risk <= 50)?(risk * 100):(risk * 70);
    let risk_color = 'red-gradient';
    if(risk <= 25) risk_color = 'blue-gradient';
    else if(risk > 25 && risk <= 50) risk_color = 'green-gradient';
    else if(risk > 50 && risk <= 75) risk_color = 'yellow-gradient';
    $('#risk').removeClass('blue-gradient').removeClass('green-gradient').removeClass('yellow-gradient').removeClass('red-gradient').addClass(risk_color);
    animateNumber(val => $('#risk').text(val+'%'), 0, risk, duration);

    let gender = $('#select-gender .gender.active').attr('id');
    let height = $('#height').val();
    let age = $('#age').attr('data-value');
    let weight = $('#weight').attr('data-value');
    let blood_pressure = $('#blood-pressure button.active').attr('data-value');
    let cholesterol = $('#cholesterol button.active').attr('data-value');
    let general_health = $('input[name=general-health]:checked').attr('data-value');
    let physical_health = $('#physical-health').attr('data-value');
    let mental_health = $('#mental-health').attr('data-value');
    let fruits = $('#fruits button.active').attr('data-value');
    let heart_attack = $('#heart-attack button.active').attr('data-value');
    // change url

}

function animateNumber(callback, from, to, duration) {
    let start = null,
        animate = timestamp => {
            start = start || timestamp;
            let progress = Math.min((timestamp - start) / duration, 1);
            callback(parseInt(progress * (to - from) + from));
            if(progress < 1) {
                window.requestAnimationFrame(animate);
            }
        };
    window.requestAnimationFrame(animate);
}

