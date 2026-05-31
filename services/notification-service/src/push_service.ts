export async function sendPushNotification(
    userId: string,
    title: string,
    body: string
) {
    console.log("PUSH NOTIFICATION");
    console.log({
        userId,
        title,
        body
    });
    return true;
}