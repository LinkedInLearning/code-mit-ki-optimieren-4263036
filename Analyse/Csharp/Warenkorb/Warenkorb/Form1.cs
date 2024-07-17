using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Warenkorb
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        List<string> warenkorb = new List<string>();
        private void button1_Click(object sender, EventArgs e)
        {
            warenkorb.Add(textBox1.Text);
            textBox2.Text += textBox1.Text + "\r\n";
            textBox1.Text = "";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string text = "";
            foreach (var item in warenkorb)
            {
                text+=item+"\n";
                
            }
            textBox2.Text = "";
            MessageBox.Show("Bestellung abgeschickt:\n"+text);
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }
    }
}
