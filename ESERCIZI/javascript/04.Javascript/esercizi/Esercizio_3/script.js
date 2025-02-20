function Statistic(grades){
    this.grades = grades;

    this.mean = function() {

        var sum = 0;
        var grade;
        for (grade of this.grades){
            sum = sum + grade;
        }

        return (sum / this.grades.length).toFixed(2);
    }

    this.minimun=  function(){
        var min = 33;
        var grade= 0;
        for (var grade of this.grades){
            min = Math.min(grade, min);
        }
        return min;
    }

    this.max = function(){
        var max = 0;
        var grade = 0;
        for (grade of this.grades){
            max = Math.max(grade, max);
        }
        return max;
    }

    this.meanError = function() {
        var mean = this.mean();

        var sumError = 0;
        var grade;
        for (grade of this.grades){
            sumError = sumError + Math.abs(grade - mean);
        }

        return (sumError / this.grades.length).toFixed(2);
    }

}

function computeStatistics() {
    // Recupera l'input dall'utente
    const inputGrades = document.getElementById('grades').value.trim();

    if (!inputGrades) {
        showError("Inserisci almeno un voto!");
        return;
    }

    // Transform votes from string to array of numbers
    var stringArray = inputGrades.split(',');
    var gradesArray = [];

    var stringValue;
    for (stringValue of stringArray){
        gradesArray.push(parseInt(stringValue.trim()));
    }

    // Filter not valid votes
    var grade;
    for (grade of gradesArray){
        if (isNaN(grade) || grade < 18 || grade > 33) {
            showError("Ogni voto deve essere un numero compreso tra 18 e 33!");
            return;
        }
    }

    // Statistic objects creation
    var statistics = new Statistic(gradesArray);

    // Show results
    document.getElementById('results').innerHTML = `
        <p><strong>Voti inseriti:</strong> ${gradesArray.join(', ')}</p>
        <p><strong>Voto minimo:</strong> ${statistics.minimun()}</p>
        <p><strong>Voto massimo:</strong> ${statistics.max()}</p>
        <p><strong>Media aritmetica:</strong> ${statistics.mean()}</p>
        <p><strong>Errore medio:</strong> ${statistics.meanError()}</p>
    `;
}

// Function to show a messag error
function showError(message) {
    // insert a paragraph with the eror message
    document.getElementById('results').innerHTML = `<p class="error">${message}</p>`;
}
