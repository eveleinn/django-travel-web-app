
// Автозаполнение фильтра по длительности (дней)
document.addEventListener("DOMContentLoaded", () => {  // ожидание полной загрузки страницы перед выполнением
	const durations = new Set();
	const items = document.querySelectorAll('.page_item');// находим все элементы тура

	items.forEach(item => {
		const duration = parseInt(item.querySelector('.duration .right').textContent.trim());
		if (!isNaN(duration)) durations.add(duration);
	});

	// Сортируем длительности по возрастанию и добавляем в select
	const durationSelect = document.getElementById('filter-duration');
	Array.from(durations)
		.sort((a, b) => a - b)
		.forEach(duration => {
			const option = document.createElement('option');
			option.value = duration;
			option.textContent = `${duration} дней`;
			durationSelect.appendChild(option);
		});
});

function applyFilters() {
	const difficulty = document.getElementById('filter-difficulty').value;
	const duration = document.getElementById('filter-duration').value;
	const maxDate = document.getElementById('filter-date').value;
	const maxPrice = document.getElementById('filter-price').value;

	const items = document.querySelectorAll('.page_item');

	items.forEach(item => {
		const itemDifficulty = item.querySelector('.difficulty .right').textContent.trim();  //извлекаем для каждого тура
		const itemDuration = parseInt(item.querySelector('.duration .right').textContent.trim());
		const itemDateRaw = item.querySelector('.date .right').textContent.trim();
		const itemPriceRaw = item.querySelector('.price .selection').textContent.replace(/\s+/g, '');

		// разбиваем строку даты на день, месяц и год
		const [day, monthName, year] = itemDateRaw.split(' ');
		const monthMap = {
			'января': '01', 'февраля': '02', 'марта': '03', 'апреля': '04', 'мая': '05',
			'июня': '06', 'июля': '07', 'августа': '08', 'сентября': '09',
			'октября': '10', 'ноября': '11', 'декабря': '12'
		};
		const itemDate = new Date(`${year}-${monthMap[monthName]}-${day}`);//сравнение даты с фильтром
		const filterDate = maxDate ? new Date(maxDate) : null;

		let visible = true;
        //Применяем каждый фильтр: если не соответствует — скрываем
		if (difficulty && difficulty !== itemDifficulty) visible = false;
		if (duration && itemDuration !== parseInt(duration)) visible = false;
		if (filterDate && itemDate > filterDate) visible = false;
		if (maxPrice && parseInt(itemPriceRaw) > parseInt(maxPrice)) visible = false;

		item.style.display = visible ? '' : 'none';
	});
}

  // Показываем модальное окно с формой бронирования
function showPhoneInput(tourId) {
    const modal = document.getElementById('phone-modal-' + tourId); //по ID тура
    modal.style.display = 'block';
    // Заполняем скрытую форму с id для соответствующего тура
    const form = document.getElementById('booking-form-' + tourId);
    form.tour_id.value = tourId; // Устанавливаем id тура в скрытое поле
}

// Функция для скрытия модального окна
function closeModal(tourId) {
    const modal = document.getElementById('phone-modal-' + tourId);
    modal.style.display = 'none';
}

