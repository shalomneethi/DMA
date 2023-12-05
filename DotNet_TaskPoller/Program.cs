using System;
using System.Net.Http;
using System.Text;
using System.Threading;
using RabbitMQ.Client;
using Newtonsoft.Json;

class Program
{
    static async Task Main()
    {
        // Define the API endpoint URL
        var apiUrl = "http://a7b54854d40364c1988b5f7ae41c14bf-252772255.ap-south-1.elb.amazonaws.com/get-starms-jobs";


        while (true) // Run indefinitely
        {
            using (var httpClient = new HttpClient())
            {
                var response = await httpClient.GetStringAsync(apiUrl);
                Console.WriteLine("Received API response: " + response);

                // Publish the API response as a message to RabbitMQ
                var factory = new ConnectionFactory()
                {
                    HostName = "a4d13d257b493465daf63c8e17fadbf6-718735712.ap-south-1.elb.amazonaws.com", // RabbitMQ server address (modify as needed)
                    UserName = "guest",
                    Password = "guest"
                };

                using (var connection = factory.CreateConnection())
                using (var channel = connection.CreateModel())
                {
                    var queueName = "job_queue"; // Replace with your RabbitMQ queue name
                    channel.QueueDeclare(queue: queueName, durable: false, exclusive: false, autoDelete: false, arguments: null);

                    // Convert the API response to a byte array
                    var body = Encoding.UTF8.GetBytes(response);

                    // Publish the message to the queue
                    channel.BasicPublish(exchange: "", routingKey: queueName, basicProperties: null, body: body);
                    Console.WriteLine("Message Sent to RabbitMQ : ");
                    Console.WriteLine(response);

                }

            }

            // Sleep for a minute before the next iteration
            Thread.Sleep(TimeSpan.FromSeconds(20));
        }
    }
}
