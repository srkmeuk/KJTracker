from flask import render_template, url_for, flash, redirect, request
from kjtracker import app, db
from kjtracker.forms import NewJewelleryRepairForm
from kjtracker.models import JewelleryRepair

# repair_data = [
#     {
#         'author': 'Seb Knight',
#         'job_number': "1",
#         'customer_name': "Jane Doe",
#         'repair_description': '18ct ring',
#         'date_created': "April 20th 2012"
#     },
#     {
#         'author': 'William Knight',
#         'job_number': "2",
#         'customer_name': "John Vil",
#         'repair_description': 'diamond watch',
#         'date_created': "January 30th 2013"
#     }
# ]


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    # repair_data = JewelleryRepair.query.all()
    page = request.args.get('page', 1, type=int)
    repair_data = JewelleryRepair.query.order_by(JewelleryRepair.booking_time.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', repair_data=repair_data)


@app.route('/jewellery_repairs/new', methods=['GET', 'POST'])
def new_jewellery_repair():
    form = NewJewelleryRepairForm()
    if form.validate_on_submit():
        jrep = JewelleryRepair(customer_name=form.customer_name.data, item_description=form.repair_description.data)
        db.session.add(jrep)
        db.session.commit()
        flash('Your new jewellery repair has been created!', 'success')
        return redirect(url_for('home'))

    return render_template('create_jewellery_repair.html', title="New Repair", form=form, legend="New Repair")


@app.route('/jewellery_repairs/<int:jrep_id>')
def jewellery_repair(jrep_id):
    jrep = JewelleryRepair.query.get_or_404(jrep_id)
    return render_template('jewellery_repair.html', title=jrep.customer_name, repair=jrep)


@app.route('/jewellery_repairs/<int:jrep_id>/update', methods=['GET', 'POST'])
def update_jewellery_repair(jrep_id):
    jrep = JewelleryRepair.query.get_or_404(jrep_id)
    form = NewJewelleryRepairForm()
    if form.validate_on_submit():
        jrep.customer_name = form.customer_name.data
        jrep.item_description = form.repair_description.data
        db.session.commit()
        flash("Repair has been updated", 'success')
        return redirect(url_for('jewellery_repair', jrep_id=jrep.id))
    elif request.method == 'GET':
        form.customer_name.data = jrep.customer_name
        form.repair_description.data = jrep.item_description

    return render_template('create_jewellery_repair.html', title="Update Repair", form=form, legend="Update Repair")


@app.route('/jewellery_repairs/<int:jrep_id>/delete', methods=['POST'])
def delete_jewellery_repair(jrep_id):
    jrep = JewelleryRepair.query.get_or_404(jrep_id)
    db.session.delete(jrep)
    db.session.commit()
    # todo make this not actually delete a record from the sql just mark a field as 'deleted' to true, this was anything every put into the system is never lost.
    #   then when accesing a repair instead of it 404'ing you can display a this has been deleted page or something, reinstate post kind of thing, aka restoring
    flash("Repair has been deleted.", 'success')
    return redirect(url_for('home'))


@app.route('/test')
def test():
    return render_template('test.html')
