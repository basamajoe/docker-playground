<html>
    <head>
        <title>Amazon products</title>
    </head>

    <body>
        <h1>Welcome to amazon web service</h1>
        <ul>
            <?php

            $json = file_get_contents('http://amazon-service/');
            $obj = json_decode($json);

            $products = $obj->products;

            foreach ($products as $product) {
                echo "<li>$product</li>";
            }

            ?>
        </ul>
    </body>
</html>
