using System.Net.Http;


var client = new HttpClient();

string json_str = @"{""func"": ""methodA"", ""in"": 1, ""out"": 2}";

var httpContent = new StringContent(json_str, Encoding.UTF8, "application/json");

var response = client.PostAsync("http://localhost:8000/", httpContent); // need await or stay alive
