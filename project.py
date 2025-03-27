from simple_blogger import SimplestBlogger
from simple_blogger.senders.TelegramSender import TelegramSender
from simple_blogger.senders.VkSender import VkSender

class Project(SimplestBlogger):
    def __init__(self, **kwargs):
        super().__init__(            
            reviewer=TelegramSender(),
            senders=[
                TelegramSender(channel_id='@have_the_nice_day'),
                VkSender(group_id='229838092')
            ],
            send_text_with_image=True,
            **kwargs)

    def _example_task_creator(self):
        return [{ 
            "topic_prompt": "Пожелай отличного дня всему миру, используй смайлики, не используй 'Конечно'"
            # ,"topic_image": "Нарисуй яркую иллюстрацию идеального дня, наполненного радостью и позитивом. Цветовая гамма теплая, яркая и солнечная, стиль мультяшный и эмоционально заряженный.",
        }]
   
    def _system_prompt(self, _):
        return f"Ты - самый оптимистичный в мире человек"
    
