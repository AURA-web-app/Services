export async function sendSMS(
    phone: string,
    message: string
) {
    console.log("SMS SENT");
    console.log({
        phone,
        message
    });
    return true;
}