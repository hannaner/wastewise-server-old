from django.db import models
# Item model

class Item(models.Model):
    name = models.CharField(max_length=250)
    quantity = models.CharField(max_length=100)
    exp_date = models.DateField(auto_now=False)
    spot_id = models.ForeignKey(
        'Spot',
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"""
        Item: {self.name}
        Quantity: {self.quantity}
        Expiring on: {self.exp_date}
        """
    
    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
            'exp_date': self.exp_date,
        }