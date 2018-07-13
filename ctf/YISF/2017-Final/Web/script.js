var _______ = new Array('당', '닙', '가 아', 'comment', '니다.', 'ID를', '멤버', '길이가', '의', ' ', '해주세', '요', '신', '내용을', '선택', '은 그룹', '입력한', '초과', '되었습', '입력');

function check_val() {
    var a = (true, false);
    if (!a) {
        if (confirm('당' + '신' + '은 그룹' + '의' + '멤버' + '가 아' + '닙' + '니다.')) {
            return false;
        } else {
            return false;
        }
    }
    return true;
}

function input() {
    var a = $.trim($("#uid").val());
    if (!a) {
        alert('comment' + 'ID를' + ' ' + '선택' + '해주세' + '요');
        return false;
    }
    var b = $.trim($("#content").val());
    if (!b) {
        alert('내용을' + ' ' + '입력' + ' ' + '해주세' + '요');
        return false;
    }
    if (getByteStrLength(b) > 2147483635) {
        alert('입력한' + ' ' + '길이가' + ' ' + '초과' + '되었습' + '니다.');
        return false;
    }
}


function input() {
    var b = $.trim($("#content").val());
    if (!b) {
        alert('내용을' + ' ' + '입력' + ' ' + '해주세' + '요');
        return false;
    }
    if (getByteStrLength(b) > 2147483635) {
        alert('입력한' + ' ' + '길이가' + ' ' + '초과' + '되었습' + '니다.');
        return false;
    }
}