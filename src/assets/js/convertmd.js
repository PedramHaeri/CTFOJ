var converter = new showdown.Converter();
converter.setOption('openLinksInNewWindow', true);
converter.setOption('strikethrough', true);
for (element of document.getElementsByClassName('showdown')) {
    var toConvert = element.getElementsByTagName('textarea')[0].value;
    element.innerHTML = DOMPurify.sanitize(converter.makeHtml(toConvert), { ADD_ATTR: ['target'] });
}
