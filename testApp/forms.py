from django import forms


class InputForm(forms.Form):
    m = [("suzuki", "Suzuki"),
         ("honda", "Honda"),
         ("toyota", "Toyota"),
         ("daihatsu", "Daihatsu"),
         ("nissan", "Nissan"),
         ("mercedes-benz", "Mercedes Benz"),
         ("mitsubishi", "Mitsubishi"),
         ("kia", "KIA")]
    c = [("karachi", "Karachi"),
         ("lahore", "Lahore"),
         ("islamabad", "Islamabad"),
         ("quetta", "Quetta"),
         ("peshawar", "Peshawar"),
         ("rawalpindi", "Rawalpindi"),
         ("hyderabad", "Hyderabad")]
    make = forms.ChoiceField(label='Make ', choices=m)
    model = forms.CharField(label='Model ', max_length=20)
    city = forms.ChoiceField(label='City', choices=c)
