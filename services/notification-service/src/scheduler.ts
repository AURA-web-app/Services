import cron from "node-cron";
import { sendPushNotification } from "./push_service";
import { sendSMS } from "./sms_service";
import { sendEmail } from "./email_service";

cron.schedule(
    "0 18 * * *",
    async () => {
        console.log(
            "Running daily study reminders..."
        );
        await sendPushNotification(
            "rudra",
            "Study Reminder",
            "Complete today's revision."
        );
        await sendSMS(
            "+911234567890",
            "Weekly test tomorrow."
        );
        await sendEmail(
            "student@example.com",
            "Exam Reminder",
            "Math exam in 3 days."
        );
    }
);