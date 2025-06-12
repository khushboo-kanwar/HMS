from django.db import models

# Create your models here.
   
class EventCategory(models.Model):  
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name        
 

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=300)
    description = models.TextField()
    organizer_name = models.CharField(max_length=200)
    organizer_email = models.EmailField()
    organizer_phone = models.CharField(max_length=15)
    special_requests = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name    

class EventBooking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=200)
    guest_email = models.EmailField()
    guest_phone = models.CharField(max_length=15)
    number_of_guests = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    special_requests = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Booking for {self.guest_name} at {self.event.name} on {self.booking_date}"         
    
class EventPayment(models.Model):   
    event_booking = models.ForeignKey(EventBooking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal')])
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.event_booking} - {self.amount}"  
    
class EventReview(models.Model):    
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=200)
    rating = models.IntegerField()  # 1 to 5
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.guest_name}'s review for {self.event.name}"  
    
class EventGalleryImage(models.Model):  
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='event_gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title       
    
class EventService(models.Model):   
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    icon = models.ImageField(upload_to='event_service_icons/', null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name    
    
class EventOffer(models.Model): 
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    percentage = models.PositiveIntegerField()  # e.g. 10%
    valid_from = models.DateField()
    valid_to = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.code})"    
    
class EventContactMessage(models.Model):    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"       
 

class EventManagement(models.Model):  
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    manager_name = models.CharField(max_length=200)
    manager_email = models.EmailField()
    manager_phone = models.CharField(max_length=15)
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Management for {self.event.name} by {self.manager_name}"
    
class Insurance(models.Model):  
    policy_number = models.CharField(max_length=100)
    provider_name = models.CharField(max_length=200)
    coverage_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Insurance for {self.event.name} - {self.provider_name}"
    
class Courier(models.Model):  
    service_name = models.CharField(max_length=200)
    service_description = models.TextField()
    service_price = models.DecimalField(max_digits=10, decimal_places=2)
    service_duration = models.DurationField()  # Duration of the service

    def __str__(self):
        return self.service_name
    
class Frieght(models.Model):  
    service_name = models.CharField(max_length=200)
    service_description = models.TextField()
    service_price = models.DecimalField(max_digits=10, decimal_places=2)
    service_duration = models.DurationField()  # Duration of the service

    def __str__(self):
        return self.service_name
    
class Calendar(models.Model):  
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return f"Calendar entry for {self.event.name} on {self.date}"

class Outlook_Calendar(models.Model):  
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return f"Outlook Calendar entry for {self.event.name} on {self.date}"
    
class Zoom_Meeting(models.Model):  
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    meeting_id = models.CharField(max_length=100)
    meeting_password = models.CharField(max_length=100)
    meeting_date = models.DateTimeField()
    meeting_duration = models.DurationField()  # Duration of the meeting

    def __str__(self):
        return f"Zoom Meeting for {self.event.name} - {self.meeting_id}"
    
class Google_Meet(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    meeting_id = models.CharField(max_length=100)
    meeting_password = models.CharField(max_length=100)
    meeting_date = models.DateTimeField()
    meeting_duration = models.DurationField()  # Duration of the meeting

    def __str__(self):
        return f"Google Meet for {self.event.name} - {self.meeting_id}"
    
class Whereby_Meeting(models.Model):  
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    meeting_id = models.CharField(max_length=100)
    meeting_password = models.CharField(max_length=100)
    meeting_date = models.DateTimeField()
    meeting_duration = models.DurationField()  # Duration of the meeting

    def __str__(self):
        return f"Whereby Meeting for {self.event.name} - {self.meeting_id}"
    
class Zoho_Meeting(models.Model):  
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    meeting_id = models.CharField(max_length=100)
    meeting_password = models.CharField(max_length=100)
    meeting_date = models.DateTimeField()
    meeting_duration = models.DurationField()  # Duration of the meeting

    def __str__(self):
        return f"Zoho Meeting for {self.event.name} - {self.meeting_id}"
    
class Livestrom_Meeting(models.Model):  
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    meeting_id = models.CharField(max_length=100)
    meeting_password = models.CharField(max_length=100)
    meeting_date = models.DateTimeField()
    meeting_duration = models.DurationField()  # Duration of the meeting

    def __str__(self):
        return f"Livestrom Meeting for {self.event.name} - {self.meeting_id}"
    
class Goto_Meeting(models.Model):  
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    meeting_id = models.CharField(max_length=100)
    meeting_password = models.CharField(max_length=100)
    meeting_date = models.DateTimeField()
    meeting_duration = models.DurationField()  # Duration of the meeting

    def __str__(self):
        return f"Goto Meeting for {self.event.name} - {self.meeting_id}"
    
class Meeting_Hub(models.Model):  
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    meeting_id = models.CharField(max_length=100)
    meeting_password = models.CharField(max_length=100)
    meeting_date = models.DateTimeField()
    meeting_duration = models.DurationField()  # Duration of the meeting

    def __str__(self):
        return f"Meeting Hub for {self.event.name} - {self.meeting_id}"
    
class Apoitment(models.Model):  
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    appointment_time = models.TimeField()
    appointment_duration = models.DurationField()  # Duration of the appointment
    appointment_description = models.TextField()

    def __str__(self):
        return f"Appointment for {self.event.name} on {self.appointment_date}"
    
class Portfolio(models.Model):  
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    portfolio_name = models.CharField(max_length=200)
    portfolio_description = models.TextField()
    portfolio_image = models.ImageField(upload_to='event_portfolio/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.portfolio_name
    
class Resume_Builder(models.Model):  
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    resume_name = models.CharField(max_length=200)
    resume_description = models.TextField()
    resume_file = models.FileField(upload_to='event_resumes/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.resume_name
    

class Reminder(models.Model):  
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    reminder_date = models.DateTimeField()
    reminder_message = models.TextField()

    def __str__(self):
        return f"Reminder for {self.event.name} on {self.reminder_date}"
    
class Workflow(models.Model):  
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    workflow_name = models.CharField(max_length=200)
    workflow_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.workflow_name
    
class Google_Sheet(models.Model):  
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    sheet_name = models.CharField(max_length=200)
    sheet_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sheet_name
    
class Spreadsheet(models.Model):  
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    spreadsheet_name = models.CharField(max_length=200)
    spreadsheet_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.spreadsheet_name
    
class Find_Google_Leads(models.Model):  
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    lead_name = models.CharField(max_length=200)
    lead_email = models.EmailField()
    lead_phone = models.CharField(max_length=15)
    lead_source = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lead: {self.lead_name} - {self.lead_source}"
    
    