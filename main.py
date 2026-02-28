import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import yfinance as yf


class LMTrades(App):
    def build(self):
        # Setting up the layout
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # 1. The Title (No Emojis)
        self.label = Label(text="TradeZen Alpha v1.0", font_size='30sp')
        self.layout.add_widget(self.label)

        # 2. The Result Display Area
        self.result_label = Label(
            text="Press button to analyze Reliance", font_size='18sp')
        self.layout.add_widget(self.result_label)

        # 3. The Action Button
        self.btn = Button(
            text="RUN ANALYSIS",
            size_hint=(1, 0.2),
            background_color=(0, 0.5, 0.8, 1)  # Professional Blue
        )
        self.btn.bind(on_press=self.run_analysis)
        self.layout.add_widget(self.btn)

        return self.layout

    def run_analysis(self, instance):
        try:
            # Fetching data for Reliance Industries
            stock = yf.Ticker("RELIANCE.NS")
            df = stock.history(period="6mo")

            # Math logic for moving averages
            short_ma = df['Close'].rolling(window=20).mean().iloc[-1]
            long_ma = df['Close'].rolling(window=50).mean().iloc[-1]
            current_price = df['Close'].iloc[-1]

            # Simple Trading Logic
            if short_ma > long_ma:
                signal = "SIGNAL: BUY"
            elif short_ma < long_ma:
                signal = "SIGNAL: SELL"
            else:
                signal = "SIGNAL: HOLD"

            # Updating the screen text
            output = f"Price: $. {current_price:.2f}\n{signal}\nAvg(20): {short_ma:.2f}\nAvg(50): {long_ma:.2f}"
            self.result_label.text = output

        except Exception:
            self.result_label.text = "Error: Check Internet Connection"


if __name__ == "__main__":
    LMTrades().run()
