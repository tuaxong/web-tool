<?php
header("Content-Type: application/json");

$latest_version = "1.0";
$file_url = "http://127.0.0.1/update-server/updates/example_app_v1.2.zip";

$response = [
    "latest" => $latest_version,
    "url" => $file_url,
    "changelog" => "Initial release."
];

echo json_encode($response);
?>