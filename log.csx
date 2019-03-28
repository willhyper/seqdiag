using System.Net.Http;

var url = new Uri("http://localhost:8000");

var client = new HttpClient { BaseAddress = url };

string json_str = @"{""func"": ""methodA"", ""in"": 1, ""out"": 2}";

var httpContent = new StringContent(json_str, Encoding.UTF8, "application/json");

var response = client.PostAsync("/", httpContent);

// public class MySender
// {

//     private HttpClient client;

//     public MySender(HttpClient c)
//     {
//         this.client = c;
//     }

//     public async Task<HttpResponseMessage> Send(string json_str)
//     {
//         var httpContent = new StringContent(json_str, Encoding.UTF8, "application/json");

//         using (HttpResponseMessage response = await client.PostAsync("/", httpContent))
//         {
//             return response;
//         }
//     }
// }

// var sender = new MySender(client);
