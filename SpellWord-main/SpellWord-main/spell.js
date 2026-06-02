// Твой список слов прямо в коде
const wordBank = {
    "easy": ["cat", "dog", "sun", "book", "ball"],
    "medium": ["garden", "winter", "forest", "orange", "player"],
    "hard": ["adventure", "knowledge", "structure", "interface", "algorithm"]
};

let correctWord = "";

function nextWord() {
    // 1. Собираем все слова в один массив
    const allWords = [...wordBank.easy, ...wordBank.medium, ...wordBank.hard];
    
    // 2. Выбираем случайное слово
    const original = allWords[Math.floor(Math.random() * allWords.length)].toLowerCase();
    correctWord = original;

    // 3. Перемешиваем буквы (аналог shuffle из Python)
    let scrambled = original.split('').sort(() => Math.random() - 0.5).join('');
    
    // Проверка: если вдруг перемешалось так, что слово не изменилось
    if (scrambled === original && original.length > 1) {
        return nextWord(); 
    }

    // 4. Выводим на экран
    document.getElementById('word-display').innerText = scrambled.toUpperCase();
    document.getElementById('result').innerText = "";
    document.getElementById('user-guess').value = "";
    document.getElementById('user-guess').focus();
}

function check() {
    const guess = document.getElementById('user-guess').value.trim().toLowerCase();
    const resultElement = document.getElementById('result');

    if (guess === correctWord) {
        resultElement.style.color = "#27ae60";
        resultElement.innerText = "✅ Правильно!";
        setTimeout(nextWord, 1500);
    } else {
        resultElement.style.color = "#e74c3c";
        resultElement.innerText = "❌ Попробуй еще раз!";
    }
}

// Запускаем первую игру при загрузке страницы
nextWord();