# Как пользоваться программой?

## Начальная настройка.
<ul>
<li> Открой файл <b>config.py </b> черех любой текстовый редактор или самый обычный блокнот.</li>
<li>Укажи путь к папке с обоями(обрати внимание на двойной j,обратный слеш).</li>
<li> Зайди в папку с обоями.</li>
</ul>

<br>

## Теперь очень важно!
<p>Необходимо указать порядок фотографий для корректной их смены в разное время суток. Сделать это нужно только так и никак иначе:</p>

Допустим, у меня есть фотография <b><i>kolyaloh.jpg</i></b> и я хочу, чтобы она стояла утром. Нужно всего лишь в конец файла дописать: <b><i>-morning</i></b>. (Обрати внимание на тире перед словом)

Теперь файл <b><i>kolyaloh.jpg</i></b> должен выглядеть так: <b><i>kolyaloh-morning.jpg</i></b> 

Аналогично с днем: <b><i>-day</i></b>,<br>
вечером <b><i>-evening</i></b>,<br>
ночью <b><i>-night</i></b><br>
(Обрати внимание на тире перед словом)

И да, расширение может быть любым, поддерживаемым самой виндой.

<br>

## Как происходит смена фотографий.

Программа каждые пять минут сверяет время, установленное на компьютере с данными по умолчанию.

<ul>
<li>до 08:00 - ночь</li>
<li>до 12:00 - утро</li>
<li>до 18:00 - день</li>
<li>до 23:00 - вечер (лучше оставить по умолчанию потому что мне лень фиксить баг)</li>
</ul>
По желанию можно поменять эти значения на свои в том же файле <b>config.py</b>.
Важно перезапустить программу после всяких изменений

<br>

## Потребление ресурсов.

Тут все очень скромно. Процессор не нагружается абсолютно, да и не его это дело хранить в памяти постоянно запущенную программу.<br>
Оперативной памяти программа потребляет около 4-5 мб, что абсолютно не сказывается на производительности компьютера. 