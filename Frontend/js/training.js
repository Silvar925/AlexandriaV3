import {questionsList, testsList, themesList, subjectList} from "./dataBase.js"
import { searchElement } from "./script.js";


function createObjectForTable(testsList, themesList, subjectList) {
    let tempTable = [];

    for (const test of testsList) {
        const theme = themesList.find(theme => theme.id === test.theme);
        const subject = subjectList.find(subject => subject.id === theme.subject);

        const tempObject = {
            "Номер": test.id,
            "subject": searchElement(subject.id, subjectList, 'name'),
            "name": test.name,
            "theme": searchElement(theme.id, themesList, 'name'),
            "class": test.class,
            "Сложность": test.complexity
        };

        tempTable.push(tempObject);
    }

    return tempTable;
}

let objectForTable = createObjectForTable(testsList, themesList, subjectList)

function loadTable(input) {
    const table = document.getElementById('table');

    // Создаем строку
    const row = document.createElement('tr');

    // Идем по свойствам входного объекта
    for (let key in input[0]) {
        // Создаем ячейку
        const cell = document.createElement('td');
        
        // Заполняем ячейку данными
        cell.innerHTML = input[0][key];
        
        // Добавляем ячейку в строку
        row.appendChild(cell);
    }

    // Добавляем строку в таблицу
    table.appendChild(row);
}

loadTable(objectForTable);
