function answer(event) {
    let answers = $(":checked");
    for(let answer of answers) {
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
let questionN = 0;
for(let question of questions) {
    form += "<p>"+question.text+"<\/p>";
    form += '<fieldset data-role="controlgroup" data-type="vertical">\n';
    let choiceN = 0;
    for(let choice of question.choices) {
	form += '<input type="radio" id="question-'+
	    questionN+'-'+choiceN+'"'+
	    ' name="question-'+questionN+'" '+
	    'value="'+choiceN+'">';
	form += '<label for="question-'+questionN+'-'+choiceN+'">'+
	    choice.text+'<\/label>\n';
	choiceN++;
    }
    form += '</fieldset>\n';
    questionN++;
}
form += '<button class="ui-btn ui-shadow" onclick="answer(event)">'+
    'Answer<\/button>';
form += "<\/form>\n";
document.getElementById("container").innerHTML = form;

