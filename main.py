from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.core.clipboard import Clipboard


class GoldLotAI(App):

    def build(self):

        self.layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        self.layout.add_widget(
            Label(text="Gold Lot AI V1", font_size=25)
        )


        self.entry = TextInput(
            hint_text="Entry (Example: 4620.469)",
            multiline=False
        )

        self.sl = TextInput(
            hint_text="Stop Loss",
            multiline=False
        )

        self.tp = TextInput(
            hint_text="Take Profit",
            multiline=False
        )


        self.layout.add_widget(self.entry)
        self.layout.add_widget(self.sl)
        self.layout.add_widget(self.tp)


        self.direction = Spinner(
            text="Select Direction",
            values=("Buy", "Sell"),
            size_hint=(1, .2)
        )

        self.layout.add_widget(self.direction)


        risks = tuple(
            str(x) for x in range(100, 2100, 100)
        )


        self.risk = Spinner(
            text="100",
            values=risks,
            size_hint=(1, .2)
        )

        self.layout.add_widget(self.risk)


        btn = Button(
            text="Calculate Lot",
            size_hint=(1,.2)
        )

        btn.bind(
            on_press=self.calculate
        )

        self.layout.add_widget(btn)


        copy = Button(
            text="Copy Signal",
            size_hint=(1,.2)
        )

        copy.bind(
            on_press=self.copy_signal
        )

        self.layout.add_widget(copy)


        self.result = Label(
            text="",
            font_size=18
        )

        self.layout.add_widget(self.result)


        return self.layout



    def calculate(self, instance):

        try:

            entry = float(self.entry.text)
            sl = float(self.sl.text)
            tp = float(self.tp.text)

            risk = int(self.risk.text)

            direction = self.direction.text


            if direction == "Buy":

                if sl >= entry:
                    self.result.text = "ERROR: Buy SL must be below Entry"
                    return


            if direction == "Sell":

                if sl <= entry:
                    self.result.text = "ERROR: Sell SL must be above Entry"
                    return



            lot = risk / (abs(entry-sl)*100)

            lot = round(lot,2)



            if direction == "Buy":

                self.signal = f"""{lot} LOT

Buy Entry: {entry:.3f}
Stop Loss: {sl:.3f}
Take Profit: {tp:.3f}
"""


            else:

                self.signal = f"""{lot} LOT

Sell Entry: {entry:.3f}
Stop Loss: {sl:.3f}
Take Profit: {tp:.3f}
"""


            self.result.text = self.signal


        except:

            self.result.text = "Invalid Input"



    def copy_signal(self, instance):

        try:
            Clipboard.copy(self.signal)
            self.result.text += "\n\nCopied!"

        except:
            pass



GoldLotAI().run()