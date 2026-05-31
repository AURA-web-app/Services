export async function sendEmail(
    to: string,
    subject: string,
    body: string
) {
    console.log("EMAIL SENT");
    console.log({
        to,
        subject,
        body
    });
    return true;
}