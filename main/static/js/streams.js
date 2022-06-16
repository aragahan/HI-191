const APP_ID = 'ab463b2c13cc40279dd71e7181ba55af'
const CHANNEL = 'main'
const TOKEN = '006ab463b2c13cc40279dd71e7181ba55afIAAJ1k93cBAWKw4yyZ1OLJjcv4Fy2eCcXtXe0aM+FNlDlmTNKL8AAAAAEADzS24fcs6rYgEAAQBxzqti'
let UID;

const client = AgoraRTC.createClient({mode:'rtc', codec:'vp8'})

let localTracks = []
let remoteUsers = {}

let joinAndDisplayLocalStream = async () => {
    UID = await client.join(APP_ID, CHANNEL, TOKEN, null)

    localTracks = await AgoraRTC.createMicrophoneAndCameraTracks()

    let player = `<div class="video-container" id="user-container-${UID}">
    <div class="username-wrapper">
        <span class="user-name"> My name </span>
    </div
    
    <div class="video-player" id="user-${UID}">
        
    </div>
    </div>`

    document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)
    localTracks[1].play(`user-${UID}`)
    await client.publish([localTracks[0], localTracks[1]])
}

joinAndDisplayLocalStream()