function syntaxHighlight(json) {
    json = json.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function (match) {
        var cls = 'number';
        if (/^"/.test(match)) {
            if (/:$/.test(match)) {
                cls = 'key';
            } else {
                cls = 'string';
            }
        } else if (/true|false/.test(match)) {
            cls = 'boolean';
        } else if (/null/.test(match)) {
            cls = 'null';
        }
        return '<span class="' + cls + '">' + match + '</span>';
    });
}

var a = [{qr_code:'http://qr.com', avarda_url:'http://user/ea13r3mke', stat:{category:'-', content_label:'-', snbt:1, fd:1}, messages:['example.msg1.com', 'example.msg2.com'], wby_account:{media_types:['wechat', 'meipai', 'miaopai'], avarda_url:'test'}, wechat_id:'iyiakwy', icon: 'http://wechat/somewhsomewhere'}]

var b = { msgs:{msgs_count:10000, top_articles:[{name:'xxxx', owner:'xxxx'}, {name:'yyyy', owner:'yyyy'}]}, stat:{msgs_count:10000, top_articles:[{name:'xxxx', owner:'xxxx'}, {name:'yyyy', owner:'yyyy'}]}}

var c = {id:'19854', msg_id:"xx-xxxx-xxxx" ,wechat_id:'iYiakwy', read_num:100, like_num:100, url:'http:exmaple.com', title:'test', created_at:'2016-09-01 00:00::00'}

console.log(JSON.stringify(a, undefined, 4));
console.log(JSON.stringify(b, undefined, 4));
console.log(JSON.stringify(c, undefined, 4));
