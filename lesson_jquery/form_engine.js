function answer(event) {
    let answers = $(":checked");
    for (let answer of answers) {
        let idMatch = answer.id.match(/question-(\d+)-(\d+)/);
        let questionN = idMatch[1];
        let choiceN = idMatch[2];
        let points = questions[questionN].choices[choiceN].points;
        console.log(answer.id, points);
    }
    event.preventDefault();
    return false;
}
let form = "<form>\n";
for (let [questionN, question] of questions.entries()) {
    form += `<p>${question.text}<\/p>`;
    form += `<fieldset data-role="controlgroup" data-type="vertical">\n`;
    for (let [choiceN, choice] of question.choices.entries()) {
        form += `<input type="radio" id="question-` +
            `${questionN}-${choiceN}" name="question-${questionN}" ` +
            `value="${choiceN}">`;
        form += `<label for="question-${questionN}-${choiceN}">` +
            `${choice.text}<\/label>\n`;
        choiceN++;
    }
    form += `</fieldset>\n`;
    questionN++;
}
form += '<button class="ui-btn ui-shadow" onclick="answer(event)">' +
    'Answer<\/button>';
form += "<\/form>\n";
document.getElementById("container").innerHTML = form;
