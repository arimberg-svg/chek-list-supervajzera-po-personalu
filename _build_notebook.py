# -*- coding: utf-8 -*-
"""Чек-лист супервайзера по персоналу — полный: СПК, ПК, РТЗ, кассир, кладовщик, МОП + свои дела."""
from pathlib import Path
import html

OUT = Path(__file__).resolve().parent / "index.html"


def esc(s):
    return html.escape(s, quote=True)


def item(text):
    return f"""
    <label class="item">
      <input type="checkbox" data-k />
      <span class="box" aria-hidden="true"></span>
      <span class="txt">{esc(text)}</span>
    </label>"""


def items(texts):
    return "\n".join(item(t) for t in texts)


def section(title, body, note=""):
    note_html = f'<p class="when">{esc(note)}</p>' if note else ""
    return f"""
    <section class="block">
      <h2>{esc(title)}</h2>
      {note_html}
      <div class="list">{body}</div>
    </section>"""


def field(label):
    return f"""
    <label class="field">
      <span>{esc(label)}</span>
      <input type="text" data-k class="ink" autocomplete="off" />
    </label>"""


# —— содержание ——
supervisor_office = [
    "Графики по курируемым магазинам сверены и актуальны",
    "Дыры в сменах закрыты: согласовано с СПК, сотрудник уведомлён",
    "Штатная расстановка по точкам сверена с фактом явки",
    "Открытые вакансии и приоритет закрытия по точкам зафиксированы",
    "Перебросы при нехватке персонала организованы и приняты точкой",
    "Явка после переброса проверена; при срыве график скорректирован",
    "Потребность в персонале актуализирована: должности, количество, срочность",
    "Собеседования проведены по скрипту / анкете должности",
    "Выход кандидата согласован: дата, смена, наставник, схема стажировки",
    "Первый день новичка проконтролирован; передача на адаптацию закрыта",
    "Сотрудники с риском увольнения выявлены; разговор проведён, причины записаны",
    "Меры удержания предложены или согласована замена и срок закрытия ставки",
    "Личные планы продаж внесены / скорректированы в 1С",
    "Планы сверены с расстановкой и открытыми ставками; СПК и сотрудники понимают цифры",
    "Новички и слабые сотрудники подключены к обучению / стажировке / тестам Академии",
    "Задачи в Битрикс24 по персоналу закрыты или с актуальным сроком",
    "Краткий отчёт руководителю: штат, риски, подбор, визиты, решения",
]

visit_start = [
    "Визит по плану объезда; магазин, дата и время зафиксированы",
    "СПК точки знает цель визита; смена представлена",
    "Внешний вид смены: форма, бейджи, опрятность",
    "TargControl: явка, опоздания, расхождения с графиком",
    "Пятиминутка / план дня на смене есть; задачи с исполнителями понятны",
    "Общий обход: улица → вход → зал → касса → склад",
]

spk = [
    "Утро: анализ вчерашнего ТО, акций, неликвидов перед пятиминуткой",
    "Пятиминутка: внешний вид, цели дня, замечания с обхода, индивидуальные задания",
    "Обход: улица, касса, зал, склад — замечания с исполнителями и сроком",
    "Уличная выкладка полная; вывески, баннеры, парковка без мусора и машин сотрудников",
    "Тачки, мотоблоки, бетономешалки собраны и стоят в ширину и в глубину, не «по одной для вида»",
    "Зал: чистота, проходы, ценники на всём выставленном, товар к продаже выставлен",
    "Пустые крючки / дыры: контроль по графику пн и чт; ТСД «Проверка крючков»; довыкладка",
    "Активная матрица, остаток 0: ценник не снят, висит «извиняшка»",
    "Акционный стеллаж и корзина распродаж актуальны",
    "Мин-максы, «извиняшки», товарное наполнение KVI / ОВТ под контролем",
    "Неликвиды 180+: остатки, вид, комплектность, знания смены; проблемный список на виду у команды",
    "Контроль кассира, ПК, РТЗ и кладовщика в течение смены — замечания закрываются в смену",
    "Очереди на кассе: причины зафиксированы, меры приняты",
    "Пересчёт кассы не реже двух раз в день с актом",
    "Контроль качества приёмки не реже двух раз в день",
    "Веерный пересчёт по графику магазина — не менее 50 SKU в день",
    "Заказы клиентов: незакрытые под контролем; срок жизни заказа 14 дней",
    "Стол заказов и интернет-заказы: сборка → оплата → выдача без зависаний",
    "Кассовый отчёт с приложениями отправлен; тема письма: магазин и период",
    "Размен на кассе под контролем; запрос размена вовремя",
    "Задачи Битрикс24: просмотр, исполнение, делегирование, закрытие, сроки",
    "Брак: зона, учёт, меры; ответственный на точке понятен",
    "Отрицательные остатки и зависшие перемещения разобраны, не только зафиксированы",
    "Первичка в офис по графику; УПД по ЭДО в месяце отгрузки",
    "Инкассация по графику / инструкции (Сберинкассация)",
    "График смен точки актуален; табель и расстановка сходятся",
    "Мотивация команды: цели понятны, обратная связь по результатам дня дана",
    "Жалобы и конфликты в зале разобраны; эскалация при необходимости",
    "Нештатные ситуации: кому звонить, знает СПК и смена",
    "Вечер: задачи дня закрыты или переданы; ответственный на вечер назначен",
]

pk = [
    "Встреча: заметил → поздоровался → назвал себя → спросил, чем помочь",
    "Сначала потребность, потом совет: что делают, где, кто будет работать, что уже куплено",
    "Оффер 2–3 варианта; совместимость объясняет до оплаты",
    "Допродажа / сопутка один раз по задаче клиента; отказ принимает спокойно",
    "Знание товара зоны: назначение, ограничение, совместимость; не обещает того, чего нет на карточке",
    "Наличие по телефону — только после проверки в 1С",
    "Поиск в Помощнике продаж, остаток, карточка — уверенно",
    "Конфликт по цене: извинение → сверка → решение через СПК → устранить причину",
    "Лояльность: QR / бонусы; приглашение в канал МАКС, где принято",
    "Доп. сервисы: доставка, погрузка, под заказ, кредит, заточка, сборка — предлагает по задаче",
    "Помощь донести / довезти до машины: предлагает сам, без ожидания просьбы",
    "Выкладка, ценники, чистота своей зоны; пустой крючок сообщает СПК в ту же смену",
    "Утренняя выкатка и вечерняя закатка своей зоны; пустое место пополняет в смену",
    "Битый / мятый / некомплект снимает с полки и сразу сообщает СПК",
    "Когда кассира нет или касса свободна — проводит оплату под своей учётной записью",
    "Цена на ценнике и на кассе совпадают; при расхождении зовёт СПК",
    "Форма, бейдж, закрытая обувь; приходит к началу смены",
    "Поручения СПК закрывает в срок; если мешает очередь — говорит об этом сразу",
    "Смотрит аналитику своих чеков за день; понимает личный план",
    "Сборка техники вместе с РТЗ на примере своей зоны — умеет показать",
    "Конец смены: зона в порядке, незакрытое передано",
]

rtz = [
    "Зона ответственности РТЗ понятна: что закрывает лично, что делает вместе со сменой",
    "Утро: выкатка уличной выкладки до открытия; список из 1С сверен",
    "Тачки собраны и стоят рядом, в ширину и в глубину; на складе нет «запасных в коробках для вида»",
    "Мотоблоки собраны и выставлены; неисправные и некомплект сразу сняты с продажи",
    "Бетономешалки и прочая крупная техника собраны, чистые, с ценником",
    "Сборка техники: последовательность, крепёж, проверка хода, ГСМ и расходники на месте",
    "Предпродажная подготовка: товар готов к показу, не «в коробке до замечания»",
    "Довыкладка полок и крючков в течение смены; брошенный товар возвращает на место",
    "Неразобранный приход не лежит в проходе: разобран или согласован со складом срок",
    "Ценники на своей зоне: есть, актуальны, формат единый; расхождение цен — СПК",
    "Чистота: вход, пол, полки, образцы, кассовая зона рядом с зоной РТЗ",
    "Проходы свободны: тележка проходит; товар не создаёт опасность",
    "Уличная зона: порядок, нет мусора, товар не мешает проходу покупателей",
    "Культура обращения с товаром: не бросает, не ставит мокрым на картон, не захламляет",
    "Помощь складу и кассе по запросу СПК без споров «это не моя зона»",
    "Вечерняя закатка улицы и зоны: товар убран или закреплён по правилам точки",
    "К концу смены зона РТЗ закрыта «под ключ»: выкладка, чистота, ценники, без хвостов",
    "СПК видит работу РТЗ по товару: выкладка, брошенное, приход, ценники, чистота — без накопления замечаний",
]

cashier = [
    "Выход за 15 минут до смены; открытие и закрытие смены по правилам",
    "Приветствие и прощание; тон спокойный",
    "Продажа наличными и картой; сумма вслух; пакет предлагает",
    "Допродажа на кассе: одна нужная вещь к покупке",
    "Карта / бонусы / промокоды / подарочный сертификат — по правилам",
    "Весовой товар и весы; работа и продажи на КСО",
    "Возврат своего магазина: чек, основания, оформление",
    "Возврат / товар из другого магазина сети: порядок и кого привлечь",
    "Размен: когда просить; сейф-пакет под камерами; внесение ДС",
    "Пересчёт кассы; прикассовая зона чистая, расходники есть",
    "Вечерний кассовый отчёт: тема письма магазин и период",
    "Инкассация по графику / инструкции (под контролем СПК)",
    "Действия при ошибке терминала и типовых сбоях кассы",
    "Печать и замена ценников у кассы; акции у кассы актуальны",
    "Очередь не стоит без реакции: зовёт помощь смены",
    "Юрлица на кассе: оплата, УПД, ЭДО — связка с МОП / СПК",
    "Чужой логин не использует; свою учётную запись не отдаёт",
]

warehouse = [
    "Обход склада и зоны приёмки: маршруты, зоны, брак, ворота",
    "1С:Торговля по складу: остаток, карточка, документы дня",
    "ТСД на складе; вечером ТСД закрыт",
    "Приёмка с РЦ: сверка, качество, повреждения ловит сразу",
    "Приёмка от поставщиков: документы и качество",
    "Непринятый товар не выставляет в зал",
    "Перемещения между магазинами под клиентов; зависшие не копит",
    "Подготовка к перемещению на РЦ или по заявке ИМ",
    "Сборка автозаказов; сборка и выдача заказов интернет-магазина",
    "Пересчёты и задания ревизионного отдела",
    "Брак: зона, учёт, меры; обычно ответственный за брак на точке",
    "Отрицательные остатки: алгоритм минуса, не «потом»",
    "FIFO / ротация; ГСМ и расходники для сборки техники в наличии",
    "Связка склад — МОП на корпоративной отгрузке",
    "Конец дня: 1С проведено, брак в зоне, ворота на ключ",
]

mop = [
    "Карточка корпоративного клиента и условия работы найдены",
    "Заказ и реализация для юрлица оформлены корректно",
    "Доверенность и комплект документов на отгрузку проверены",
    "УПД в день отгрузки; подписание в том же календарном месяце",
    "Работа в ЭДО без критичных ошибок",
    "Стол заказов / монитор ИМ: сборка → оплата → «Выдача заказа» один раз → СФ",
    "Резервы: нет товара — «по мере поступления»; есть — «на складе»",
    "Срок жизни заказа 14 дней — под контролем",
    "Связка МОП — склад — касса на отгрузке понятна всем троим",
    "Типовые вопросы и возражения юрлица отрабатывает спокойно",
]

visit_end = [
    "Эффективность в зале / на кассе / на складе / у РТЗ оценена по факту смены",
    "Кандидаты «под замену» и сотрудники с потенциалом роста отмечены",
    "Обратная связь СПК и линейному персоналу дана по итогам визита",
    "Проблемы точки (персонал, сервис, дисциплина) зафиксированы",
    "Эскалация руководителю сделана, если точка сама не тянет",
    "Комфорт и конфликты на точке: разговор состоялся, меры понятны",
    "Обучение / доучивание назначено конкретным людям со сроком",
    "Задачи после визита стоят в Битрикс24: что / кто / срок / критерий «готово»",
]

sections_html = "".join([
    section(
        "1. Дела супервайзера по персоналу",
        items(supervisor_office),
        "Графики, штат, подбор, удержание, планы, обучение, отчётность — вне и между визитами",
    ),
    section(
        "2. Визит на точку. Вход",
        items(visit_start),
        "Перед разбором должностей: явка, внешний вид, план дня, общий обход",
    ),
    section(
        "3. СПК. Полный контроль",
        items(spk),
        "Смена, зал, цифры, команда, касса, склад, задачи. Эталон — регламент и обязанности СПК",
    ),
    section(
        "4. Продавец-консультант (ПК). Полный контроль",
        items(pk),
        "Продажа, зона, сервис, касса при необходимости, аналитика чеков. Эталон — стандарт ПК",
    ),
    section(
        "5. Работник торгового зала (РТЗ). Полный контроль",
        items(rtz),
        "Улица, сборка техники, выкладка, чистота, ценники, закатка. Зона к концу смены закрыта",
    ),
    section(
        "6. Кассир. Полный контроль",
        items(cashier),
        "Смена, продажа, возврат, размен, отчёт, инкассация, очередь",
    ),
    section(
        "7. Кладовщик. Полный контроль",
        items(warehouse),
        "Приёмка, перемещения, заказы, брак, минусы, закрытие склада",
    ),
    section(
        "8. МОП, стол заказов и юрлица",
        items(mop),
        "Корпоративные отгрузки, ЭДО, монитор ИМ, связка со складом и кассой",
    ),
    section(
        "9. Итог визита",
        items(visit_end),
        "Оценка людей, обратная связь, задачи, эскалация",
    ),
])

doc = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Чек-лист супервайзера по персоналу — Академия УМ</title>
  <meta name="description" content="Полный чек-лист супервайзера по персоналу: СПК, ПК, РТЗ, кассир, кладовщик, МОП. Академия УМ." />
  <meta name="theme-color" content="#222222" />
  <style>
    :root {{
      --ink: #222222;
      --muted: #666666;
      --soft: #888888;
      --paper: #ffffff;
      --line: #cccccc;
      --page-w: 210mm;
      --font: Arial, "Helvetica Neue", Helvetica, sans-serif;
    }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      margin: 0;
      color: var(--ink);
      font-family: var(--font);
      font-size: 15px;
      line-height: 1.45;
      background: #f0f0f0;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }}

    .toolbar {{
      position: sticky; top: 0; z-index: 50;
      display: flex; flex-wrap: wrap; gap: 8px; align-items: center;
      justify-content: space-between;
      padding: 8px 12px;
      background: #555;
      color: #fff;
      font-size: 12px;
      font-weight: 400;
    }}
    .toolbar .brand {{
      display: flex; align-items: center; gap: 8px;
    }}
    .toolbar .brand img {{
      height: 28px; width: auto;
      background: #fff; padding: 2px 4px;
      filter: grayscale(1) opacity(0.85);
    }}
    .toolbar .actions {{ display: flex; flex-wrap: wrap; gap: 6px; align-items: center; }}
    .toolbar button {{
      border: 1px solid #ccc;
      background: transparent;
      color: #fff;
      font: inherit;
      font-size: 12px;
      padding: 5px 10px;
      cursor: pointer;
    }}
    .toolbar button.primary {{ background: #fff; color: #444; border-color: #fff; }}
    .toolbar button:hover {{ background: #666; }}
    .toolbar .status {{ font-size: 11px; opacity: .85; }}

    .sheet-wrap {{
      width: min(var(--page-w), calc(100% - 16px));
      margin: 12px auto 32px;
    }}
    .sheet {{
      background: var(--paper);
      border: 1px solid #bbb;
      box-shadow: 0 1px 6px rgba(0,0,0,.08);
      padding: 16px 18px 22px;
      font-size: 15px;
      line-height: 1.45;
    }}

    .motto {{
      text-align: center;
      font-weight: 400;
      color: #888;
      font-size: 12px;
      margin: 0 0 8px;
      letter-spacing: .04em;
    }}
    .title-block {{
      text-align: center;
      margin: 0 0 14px;
      padding: 0 0 10px;
      border-bottom: 1px solid #ccc;
    }}
    .title-block .logo {{
      display: block;
      width: min(140px, 42%);
      height: auto;
      margin: 0 auto 6px;
      filter: grayscale(1) opacity(0.75);
    }}
    .eyebrow {{
      margin: 0;
      font-size: 11px;
      color: #999;
      font-weight: 400;
    }}
    h1 {{
      font-weight: 600;
      font-size: 18px;
      line-height: 1.25;
      margin: 4px 0 2px;
      color: #555;
    }}

    .meta {{
      display: grid;
      gap: 8px;
      margin: 0 0 12px;
    }}
    .field {{
      display: grid;
      grid-template-columns: 200px 1fr;
      gap: 8px;
      align-items: end;
      font-size: 14px;
    }}
    .field span {{ color: #444; padding-bottom: 2px; }}
    .field .ink, .admit .ink {{
      border: none;
      border-bottom: 1px solid #999;
      background: transparent;
      font: inherit;
      font-size: 15px;
      padding: 2px 4px;
      color: var(--ink);
      width: 100%;
      min-width: 0;
    }}
    .field .ink:focus, .admit .ink:focus {{ outline: none; border-bottom-color: #555; }}

    .scheme {{
      margin: 0 0 16px;
      font-size: 13px;
      color: #555;
      line-height: 1.45;
    }}
    .scheme b {{ font-weight: 600; color: #444; }}

    .toc {{
      margin: 0 0 16px;
      padding: 10px 12px;
      border: 1px solid #ddd;
      font-size: 13px;
      color: #555;
      line-height: 1.5;
    }}
    .toc b {{ color: #444; }}

    .block {{
      margin: 0 0 16px;
      page-break-inside: avoid;
    }}
    h2 {{
      font-weight: 600;
      font-size: 16px;
      line-height: 1.3;
      color: #444;
      margin: 0 0 6px;
      page-break-after: avoid;
    }}
    .when {{
      margin: 0 0 8px;
      font-size: 13px;
      color: #777;
    }}
    .list {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .item {{
      display: grid;
      grid-template-columns: 18px 1fr;
      gap: 8px;
      align-items: start;
      cursor: pointer;
      font-size: 15px;
      line-height: 1.4;
    }}
    .item input {{
      position: absolute;
      opacity: 0;
      width: 1px;
      height: 1px;
      pointer-events: none;
    }}
    .item .box {{
      width: 16px;
      height: 16px;
      margin-top: 2px;
      border: 1.5px solid #666;
      background: #fff;
      flex: 0 0 auto;
    }}
    .item input:checked + .box {{
      background: #555;
      border-color: #555;
      box-shadow: inset 0 0 0 2px #fff;
    }}
    .item .txt {{ color: var(--ink); }}

    .admit {{
      margin: 18px 0 12px;
      padding-top: 12px;
      border-top: 1px solid #ccc;
      page-break-inside: avoid;
    }}
    .admit h2 {{ margin-bottom: 10px; }}
    .admit-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px 18px;
      align-items: center;
      margin: 0 0 10px;
      font-size: 15px;
    }}
    .admit-row .choice {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
    }}
    .admit-row .choice input {{ width: 16px; height: 16px; }}
    .sign {{
      display: grid;
      gap: 8px;
      margin-top: 8px;
    }}
    .sign .field {{ grid-template-columns: 180px 1fr; }}

    @media (max-width: 640px) {{
      .field, .sign .field {{ grid-template-columns: 1fr; gap: 2px; }}
      .sheet {{ padding: 12px; }}
    }}

    @media print {{
      .toolbar {{ display: none !important; }}
      body {{ background: #fff; font-size: 14px; }}
      .sheet-wrap {{ width: 100%; margin: 0; }}
      .sheet {{
        border: none;
        box-shadow: none;
        padding: 0;
      }}
      .title-block .logo {{
        width: 110px;
        filter: grayscale(1) opacity(0.55);
      }}
      h1 {{ color: #666; font-size: 16px; font-weight: 600; }}
      h2 {{ color: #555; font-size: 14px; font-weight: 600; }}
      .item {{ font-size: 13px; gap: 6px; }}
      .item .box {{ width: 13px; height: 13px; border-width: 1px; }}
      .field .ink, .admit .ink {{ border-bottom-color: #aaa; }}
      .block {{ break-inside: avoid; }}
      a {{ color: inherit; text-decoration: none; }}
    }}
  </style>
</head>
<body>
  <div class="toolbar" role="banner">
    <div class="brand">
      <img src="assets/logo.png" alt="У Михалыча" width="120" height="36" />
      <span>Академия УМ · чек-лист супервайзера по персоналу</span>
    </div>
    <div class="actions">
      <span class="status" id="save-status">онлайн-сохранение в этом браузере</span>
      <button type="button" id="btn-save">Сохранить</button>
      <button type="button" id="btn-clear">Очистить</button>
      <button type="button" class="primary" id="btn-print">Печать / PDF</button>
    </div>
  </div>

  <div class="sheet-wrap">
    <article class="sheet" id="checklist">
      <p class="motto">Делаем мир крепче</p>
      <header class="title-block">
        <img class="logo" src="assets/logo.png" alt="У Михалыча" width="250" height="72" />
        <p class="eyebrow">Академия УМ · сеть «У Михалыча»</p>
        <h1>Чек-лист супервайзера по персоналу</h1>
      </header>

      <div class="meta">
        {field("Супервайзер по персоналу")}
        {field("Магазин / точка")}
        {field("СПК точки")}
        {field("Дата визита")}
        {field("С кем смотрели смену")}
      </div>

      <p class="scheme">
        <b>Зачем лист.</b> Один объёмный чек-лист на дела супервайзера и на полный разбор всех должностей розницы на точке:
        СПК, ПК, РТЗ, кассир, кладовщик, МОП. Отметки хранятся в браузере. Лист можно напечатать.
      </p>

      <div class="toc">
        <b>Содержание.</b>
        1. Дела супервайзера ·
        2. Вход на визит ·
        3. СПК ·
        4. ПК ·
        5. РТЗ ·
        6. Кассир ·
        7. Кладовщик ·
        8. МОП и заказы ·
        9. Итог визита
      </div>

      {sections_html}

      <section class="admit">
        <h2>Закрытие визита</h2>
        <div class="admit-row">
          <span>Точка по персоналу:</span>
          <label class="choice"><input type="checkbox" data-k /> в норме</label>
          <label class="choice"><input type="checkbox" data-k /> есть риски</label>
          <label class="choice"><input type="checkbox" data-k /> нужна срочная замена / усиление</label>
        </div>
        <div class="admit-row">
          <span>Разбор должностей закрыт:</span>
          <label class="choice"><input type="checkbox" data-k /> СПК</label>
          <label class="choice"><input type="checkbox" data-k /> ПК</label>
          <label class="choice"><input type="checkbox" data-k /> РТЗ</label>
          <label class="choice"><input type="checkbox" data-k /> кассир</label>
          <label class="choice"><input type="checkbox" data-k /> кладовщик</label>
          <label class="choice"><input type="checkbox" data-k /> МОП</label>
        </div>
        {field("Главный риск / дыра")}
        {field("Что сделать до следующего визита")}
        <div class="sign">
          {field("Подпись супервайзера")}
          {field("Подпись СПК точки")}
          {field("Дата")}
        </div>
      </section>
    </article>
  </div>

  <script>
  (function () {{
    const KEY = "um-academy-supervisor-personnel-checklist-v1";
    const root = document.getElementById("checklist");
    const status = document.getElementById("save-status");
    const fields = () => root.querySelectorAll("[data-k]");

    function assignIds() {{
      fields().forEach((el, i) => {{
        if (!el.dataset.id) el.dataset.id = "f" + i;
      }});
    }}

    function collect() {{
      const data = {{}};
      fields().forEach((el) => {{
        const id = el.dataset.id;
        if (el.type === "checkbox") data[id] = el.checked;
        else data[id] = el.value;
      }});
      return data;
    }}

    function apply(data) {{
      if (!data) return;
      fields().forEach((el) => {{
        const id = el.dataset.id;
        if (!(id in data)) return;
        if (el.type === "checkbox") el.checked = !!data[id];
        else el.value = data[id] || "";
      }});
    }}

    function save(manual) {{
      try {{
        localStorage.setItem(KEY, JSON.stringify(collect()));
        const t = new Date();
        status.textContent = (manual ? "сохранено " : "автосохранение ") +
          t.toLocaleTimeString("ru-RU", {{ hour: "2-digit", minute: "2-digit" }});
      }} catch (e) {{
        status.textContent = "не удалось сохранить (память браузера)";
      }}
    }}

    function load() {{
      try {{
        const raw = localStorage.getItem(KEY);
        if (raw) apply(JSON.parse(raw));
      }} catch (e) {{ /* ignore */ }}
    }}

    assignIds();
    load();

    let timer;
    root.addEventListener("input", () => {{
      clearTimeout(timer);
      timer = setTimeout(() => save(false), 400);
    }});
    root.addEventListener("change", () => save(false));

    document.getElementById("btn-save").addEventListener("click", () => save(true));
    document.getElementById("btn-print").addEventListener("click", () => {{
      save(true);
      window.print();
    }});
    document.getElementById("btn-clear").addEventListener("click", () => {{
      if (!confirm("Очистить все отметки и поля в этом браузере?")) return;
      fields().forEach((el) => {{
        if (el.type === "checkbox") el.checked = false;
        else el.value = "";
      }});
      localStorage.removeItem(KEY);
      status.textContent = "очищено";
    }});
  }})();
  </script>
</body>
</html>
"""

OUT.write_text(doc, encoding="utf-8")
print("OK", OUT, "bytes", OUT.stat().st_size)
print("items", sum(len(x) for x in [
    supervisor_office, visit_start, spk, pk, rtz, cashier, warehouse, mop, visit_end
]))
