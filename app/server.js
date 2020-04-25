var PROTO_PATH = 'proto/meeting.proto';
var grpc = require('grpc');
var protoLoader = require('@grpc/proto-loader');

var packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true
    });

var meeting = grpc.loadPackageDefinition(packageDefinition).meeting;
var city_list = {
    'Londyn': {
        'city': 'Londyn',
        'free_places': 3,
        'participants': [
            'Hubert',
            'Krzysztof',
        ]
    },
    'Paryz': {
        'city': 'Paryz',
        'free_places': 4,
        'participants': [
            'Krzysztof',
            'Grzesiek'
        ]
    },
    'Monachium': {
        'city': 'Monachium',
        'free_places': 5,
        'participants': [
            'Hubert',
            'Grzesiek'
        ]
    }
}

function sleep(millis) {
    return new Promise(resolve => setTimeout(resolve, millis));
}

async function meetingStream(call) {
    console.log('Someone subscribed on ' + call.request.city)
    while (true) {
        await sleep(1000)
        var city = call.request.city;
        var status = call.status;
        if (status.code === 0) {
            if (city_list[city] !== undefined) {
                console.log(city)
                call.write(city_list[city]);
            } else {
                console.log('Wrong city')
                break;
            }
        } else if (status.code === 2) {
            console.log("Participant finished")
            break;
        } else if (status.code === 'ERR_STREAM_WRITE_AFTER_END') {
            console.log("Error occurred")
            break;
        }
    }
    call.end()
}

function getServer() {
    var server = new grpc.Server();
    server.addService(meeting.MeetingService.service, {
        MeetingStream: meetingStream,
    });
    return server;
}

var routeServer = getServer();
routeServer.bind('0.0.0.0:50051', grpc.ServerCredentials.createInsecure());
routeServer.start();