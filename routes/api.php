<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\Http;
use App\Jobs\ProcessFastAPIRequest;

Route::middleware(['auth:sanctum'])->get('/user', function (Request $request) {
    return $request->user();
});

Route::get('/hello-from-fastapi', function () {
    $response = Http::get('http://fastapi:8000/hello');
    return $response->json();
});

// 新增的异步处理路由
Route::post('/process-excel', function (Request $request) {
    ProcessFastAPIRequest::dispatch($request->all());
    return response()->json(['message' => 'Request queued for processing']);
});